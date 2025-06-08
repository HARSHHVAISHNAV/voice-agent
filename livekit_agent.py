import urllib.parse
import asyncio
import websockets

LIVEKIT_URL = "wss://voiceagent-qh8un4gz.livekit.cloud"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJBUElzRHZyeVU4aWNSWVAiLCJzdWIiOiJ2b2ljZS1hZ2VudCIsImF1ZCI6ImxpdmVraXQiLCJuYmYiOjE3NDkzNzcyMzEsImV4cCI6MTc0OTM4NDQzMSwicm9vbSI6InRlc3Qtcm9vbSIsInZpZGVvIjpmYWxzZSwiYXVkaW8iOnRydWUsImNhbl9wdWJsaXNoIjp0cnVlLCJjYW5fc3Vic2NyaWJlIjp0cnVlfQ.SkG53WotcY_Eib5N6iXUnJ-XnfZKdSZoZHR5wU8_tYg"  

async def connect_livekit():
    token_encoded = urllib.parse.quote(TOKEN)
    uri = f"{LIVEKIT_URL}/rtc?access_token={token_encoded}"
    async with websockets.connect(uri) as websocket:
        print("✅ Connected to LiveKit WebSocket")

        while True:
            msg = await websocket.recv()
            print(f"📥 Received: {msg}")

if __name__ == "__main__":
    asyncio.run(connect_livekit())
