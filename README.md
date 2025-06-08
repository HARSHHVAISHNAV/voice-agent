Voice Agent AI is a real-time conversational voice assistant built using LiveKit's audio streaming platform combined with powerful AI models for speech recognition, natural language understanding, and speech synthesis. The system listens to live audio in a virtual room, transcribes speech to text using a Whisper-based model, generates intelligent responses through a language model (LLM), and replies back with natural, human-like voice using ElevenLabs' text-to-speech API.

This project aims to demonstrate a full-stack voice AI pipeline integrating modern open-source and cloud technologies, designed for real-time interaction scenarios like virtual assistants, voice chatbots, and accessibility tools.

✅ Copy & Save as README.md in your project root:
markdown
Copy
Edit
# 🗣️ Voice Agent AI (LiveKit + STT + LLM + TTS)

A **real-time voice assistant** powered by [LiveKit](https://livekit.io/), **faster-whisper** (STT), **OpenAI** (LLM), and **ElevenLabs** (TTS). This bot joins a LiveKit room, listens to voice input, generates intelligent responses using an LLM, and replies back using human-like synthesized speech.

---

## 🎯 Features

- 🎧 Real-time **voice capture** from LiveKit room
- 🧠 **Speech-to-Text** using [Faster-Whisper](https://github.com/guillaumekln/faster-whisper)
- 🤖 AI-generated replies using **OpenAI LLMs**
- 🔊 Text-to-Speech responses using [ElevenLabs](https://www.elevenlabs.io/)
- 🌐 Environment-configurable and production-ready

---

## 🛠️ Setup Instructions

### 1. 🔁 Clone the repository


git clone https://github.com/HARSHHVAISHNAV/voice-agent.git
cd voice-agent

###2. 📦 Install dependencies
Use a virtual environment (recommended):

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # on Windows
# source venv/bin/activate   # on Linux/Mac
Then install required packages:

bash
Copy
Edit
pip install -r requirements.txt
###3. 🔐 Setup .env file
Create a .env file in the root with the following content:

env
Copy
Edit
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
LIVEKIT_URL=ws://your-livekit-url
ROOM_NAME=your_room_name
BOT_NAME=your_bot_name

TOGETHER_API_KEY=your_openai_or_together_ai_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
Make sure your LiveKit room is accessible and your ElevenLabs API key is valid.

▶️ Running the Voice Agent
After setting up everything:

bash
Copy
Edit
python voice_agent.py
If all works correctly, you’ll see:

bash
Copy
Edit
✅ Joined room: your_room_name as your_bot_name
🎤 Listening to: ...
💬 You said: Hello, what's up?
🔊 Replying using ElevenLabs TTS...
📦 Output Overview
Logs each transcription in real time

Responds with LLM + ElevenLabs voice

Debug-friendly and modular for further extension

💡 Notes
The .gitignore file prevents pushing heavy dependencies like venv/, .env, and DLLs

Uses faster-whisper for CPU-based STT (can be upgraded to GPU)

You must have your own LiveKit server or use LiveKit Cloud

🧩 Tech Stack
Tool	Role
LiveKit	Real-time audio streaming
Faster-Whisper	Speech-to-Text (STT)
OpenAI / Together AI	LLM-based responses
ElevenLabs	Voice-based TTS
Python	Backend logic

🙌 Contributing
If you'd like to contribute:

Fork this repo

Create a new branch: git checkout -b feature/your-feature-name

Commit your changes: git commit -m 'Added feature X'

Push to the branch: git push origin feature/your-feature-name

Open a Pull Request 🚀

👤 Author
 Harsh Vaishnav

GitHub: https://github.com/HARSHHVAISHNAV

LinkedIn: www.linkedin.com/in/harsh-vaishnav-a8b46b230

📸 Preview
Coming Soon – Live demo or sample recording!
