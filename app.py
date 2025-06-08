import os
import time
import whisper
import sounddevice as sd
from scipy.io.wavfile import write
from elevenlabs import play, ElevenLabs
import pandas as pd
from dotenv import load_dotenv
import together  

# Load API keys from .env
load_dotenv()
together_api_key = os.getenv("TOGETHER_API_KEY")
elevenlabs_api_key = os.getenv("ELEVENLABS_API_KEY")

# Set Together API key via env (recommended)
together.api_key = together_api_key

# Instantiate ElevenLabs client
elevenlabs_client = ElevenLabs(api_key=elevenlabs_api_key)

# Constants
DURATION = 5  # Record duration in seconds
FILENAME = "input.wav"
SAMPLE_RATE = 44100

# Load Whisper model
print("🔈 Loading Whisper model...")
whisper_model = whisper.load_model("base")

# Record voice
def record_voice():
    print("🎤 Recording for 5 seconds...")
    audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
    sd.wait()
    write(FILENAME, SAMPLE_RATE, audio)
    print("✅ Recording saved as input.wav")

# Transcribe speech
def transcribe_audio():
    print("🧠 Transcribing with Whisper...")
    start = time.time()
    result = whisper_model.transcribe(FILENAME)
    text = result["text"]
    eou_delay = time.time() - start
    print(f"📝 You said: {text.strip()}")
    return text.strip(), eou_delay

# Get reply from Together LLM
def get_llm_response(prompt):
    print("💬 Getting LLM response...")
    start = time.time()

    response = together.Complete.create(
        prompt=f"<|system|>\nYou are a helpful assistant.<|end|>\n<|user|>\n{prompt}<|end|>\n<|assistant|>\n",
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        max_tokens=200,
        temperature=0.7,
        stop=["<|end|>"]
    )

    ttft = time.time() - start
    reply = response['choices'][0]['text'].strip()
    print(f"LLM reply: {reply}")
    return reply, ttft

# Convert reply to speech
def speak_reply(reply_text):
    print("🗣️ Converting to speech...")
    start = time.time()
    
    audio = elevenlabs_client.text_to_speech.convert(
        text=reply_text,
        voice_id="EXAVITQu4vr4xnSDxMaL"  # Rachel
    )
    
    play(audio)  # Use the imported 'play' function here
    ttfb = time.time() - start
    return ttfb

# Log metrics
def log_metrics(eou_delay, ttft, ttfb):
    total_latency = eou_delay + ttft + ttfb
    row = {
        "EOU Delay (s)": round(eou_delay, 2),
        "TTFT (s)": round(ttft, 2),
        "TTFB (s)": round(ttfb, 2),
        "Total Latency (s)": round(total_latency, 2)
    }
    df = pd.DataFrame([row])
    df.to_csv("metrics.csv", mode='a', header=not os.path.exists("metrics.csv"), index=False)
    print(f"📊 Metrics logged: {row}")

# Run the full pipeline
if __name__ == "__main__":
    record_voice()
    user_text, eou_delay = transcribe_audio()
    if user_text.strip() == "":
        print("⚠️ No speech detected. Please try again.")
    else:
        reply, ttft = get_llm_response(user_text)
        ttfb = speak_reply(reply)
        log_metrics(eou_delay, ttft, ttfb)
