import jwt
import time
import os
import urllib.parse
import asyncio
import websockets
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("LIVEKIT_API_KEY")
API_SECRET = os.getenv("LIVEKIT_API_SECRET")

def create_token():
    current_time = int(time.time())
    payload = {
        "iss": API_KEY,
        "sub": "voice-agent",
        "aud": "livekit",
        "nbf": current_time,
        "exp": current_time + 3600,
        "can_publish": True,
        "can_subscribe": True,
    }

    token = jwt.encode(payload, API_SECRET, algorithm="HS256")
    if isinstance(token, bytes):
        token = token.decode("utf-8")
    return token

async def connect_livekit(token):
    LIVEKIT_URL = "wss://voiceagent-qh8un4gz.livekit.cloud"
    token_encoded = urllib.parse.quote(token)
    uri = f"{LIVEKIT_URL}/rtc?access_token={token_encoded}"

    async with websockets.connect(uri) as websocket:
        print("✅ Connected to LiveKit WebSocket")
        while True:
            msg = await websocket.recv()
            print(f"📥 Received: {msg}")

if __name__ == "__main__":
    token = create_token()
    print("🔐 JWT Token:", token)
    asyncio.run(connect_livekit(token))
