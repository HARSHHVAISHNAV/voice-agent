# 🧠 InvisioVoice: Real-Time AI Voice Agent using LiveKit + STT + LLM + TTS

Welcome to **InvisioVoice**, an AI-powered real-time voice agent designed to simulate human-like interaction using a streaming audio pipeline. This project uses LiveKit to manage voice sessions and integrates APIs for **Speech-to-Text**, **LLM response**, and **Text-to-Speech**, providing a full-duplex voice assistant experience.

---

## 🚀 Features

- 🎤 **Voice Input** using microphone recording
- 🧠 **Speech-to-Text (STT)** with **Together AI (Whisper-based)**
- 💬 **LLM Replies** using **Groq** (Mistral-8x7B)
- 🔊 **Text-to-Speech (TTS)** with **ElevenLabs**
- ⏱️ **Session metrics logging**: EOU Delay, TTFT, TTFB, Total Latency
- ✅ Uses LiveKit for real-time session orchestration

---

## 📂 Project Files Overview

### 1. `myagent.py` ✅
- A **fully integrated voice agent** using Together (STT), Groq (LLM), and ElevenLabs (TTS).
- Working implementation with **LiveKit session + manual voice recording**.
- ❌ Interruption handling not yet implemented.
- ❌ Latency not under 2s — but all logs are recorded to `metrics.csv`.

---

### 2. `apps.py` ⚠️
- The **ideal architecture** using VAD (Voice Activity Detection) from Silero to handle **interruptions**.
- Intended for **streaming/real-time STT** sessions.
- ❌ Currently blocked due to **ONNX compatibility issues with Python 3.12**.

---

### 3. `app.py` ✅
- A **basic working pipeline** for testing STT → LLM → TTS without LiveKit.
- Good for **offline/local experimentation** and fast debugging.

---

## 🔧 Installation & Setup

Step 1: Clone the Repository


git clone https://github.com/your-username/invisio-voice.git
cd invisio-voice

---

Step 2: Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate  # On macOS/Linux

---

Step 3: Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
Step 4: Set Up Environment Variables
Copy the sample environment file:

bash
Copy
Edit
cp .env.sample .env
Edit .env and fill in your API keys:

ini
Copy
Edit
TOGETHER_API_KEY=your-together-api-key
GROQ_API_KEY=your-groq-api-key
ELEVENLABS_API_KEY=your-elevenlabs-key

LIVEKIT_URL=your-livekit-url
LIVEKIT_API_KEY=your-livekit-key
LIVEKIT_API_SECRET=your-livekit-secret
▶️ Running the Agent
Option 1: Run Local Manual Voice Agent (Stable)
bash
Copy
Edit
python myagent.py connect --room=your-room-name
This is the most stable and production-ready version so far.

📊 Output Metrics
Session metrics are logged into:

metrics.csv: Logs for each session including:

EOU Delay (End of User speech)

TTFT (Time to First Token)

TTFB (Time to First Byte of TTS)

Total Latency

⚠️ Known Issues
apps.py uses ONNX-dependent VAD, which breaks with Python 3.12+

myagent.py does not yet support interruptions

Latency is slightly higher than 2s in most cases due to multiple API hops

💡 Future Improvements
 Migrate to Python 3.10 to fix ONNX/VAD issues

 Add streaming STT using LiveKit Ingress

 Optimize latency using async batch processing

 Add UI or CLI interface for configuration

🙌 Credits
LiveKit – Real-time voice infrastructure

Together AI – Whisper-based speech-to-text

Groq – Ultra-fast Mistral LLM responses

ElevenLabs – Human-like text-to-speech

Silero VAD – Voice Activity Detection (planned)

📜 License
This project is for educational and demo purposes. Contact the author for licensing details.
