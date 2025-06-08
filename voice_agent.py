import os
import asyncio
from dotenv import load_dotenv
from livekit import Room, create_access_token
from faster_whisper import WhisperModel
from elevenlabs import generate, play, set_api_key

# Load environment
load_dotenv()

LIVEKIT_API_KEY = os.getenv("LIVEKIT_API_KEY")
LIVEKIT_API_SECRET = os.getenv("LIVEKIT_API_SECRET")
LIVEKIT_URL = os.getenv("LIVEKIT_URL")
ROOM_NAME = os.getenv("ROOM_NAME")
BOT_NAME = os.getenv("BOT_NAME")

set_api_key(os.getenv("ELEVENLABS_API_KEY"))

model = WhisperModel("base", device="cpu")

async def main():
    token = create_access_token(
        api_key=LIVEKIT_API_KEY,
        api_secret=LIVEKIT_API_SECRET,
        identity=BOT_NAME,
        name=BOT_NAME,
    )
    token.add_grant(room_join=True, room=ROOM_NAME)

    async with Room.connect(LIVEKIT_URL, token.to_jwt()) as room:
        print(f"✅ Joined room: {ROOM_NAME} as {BOT_NAME}")
        async for track in room.subscribe_audio():
            print(f"🎤 Listening to: {track.sid}")
            async for audio_frame in track:
                samples = audio_frame.to_ndarray()
                segments, _ = model.transcribe(samples, language="en")
                text = " ".join([seg.text for seg in segments])
                if text.strip():
                    print(f"💬 You said: {text}")
                    reply = f"You said: {text}"
                    audio = generate(text=reply, voice="Bella", model="eleven_monolingual_v1")
                    play(audio)

if __name__ == "__main__":
    asyncio.run(main())
