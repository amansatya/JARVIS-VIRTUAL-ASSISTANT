# 🚀 JARVIS Virtual Assistant

A Python-powered **AI assistant** that performs tasks like **web searching, playing music, fetching news, and answering questions** using **Google Gemini API**.

---

## 📖 Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Demo Video](#demo-video)
- [Contributing](#contributing)
- [License](#license)

---

## 📝 Introduction
JARVIS is a **voice-controlled AI assistant** inspired by Iron Man's J.A.R.V.I.S. It uses **Google Gemini AI** for **natural language processing**, **speech recognition**, and **text-to-speech conversion** to interact with users in real-time.

---

## ✨ Features
- 🎙️ **Voice Recognition** - Activates using the wake word **"Jarvis"**.
- 🔍 **AI-Powered Responses** - Uses **Google Gemini AI** to answer queries.
- 🌍 **Web Browsing** - Opens websites like **Google, YouTube, Instagram, LinkedIn, GitHub**.
- 🎵 **Music Playback** - Plays pre-defined songs from YouTube.
- 📰 **News Fetching** - Retrieves the latest news headlines.
- 🗣️ **Text-to-Speech (TTS)** - Speaks responses using `gTTS`.
- 🎧 **Streaming Output** - Starts speaking while generating responses.

---

## 🛠️ Tech Stack
- **Programming Language**: Python
- **AI Model**: Google Gemini API
- **Libraries Used**:
  - `speech_recognition` - Voice input processing.
  - `google-generativeai` - AI model interaction.
  - `gTTS` - Text-to-Speech conversion.
  - `pygame` - Audio playback.
  - `requests` - Fetching news and web requests.
  - `pyttsx3` - Offline speech synthesis.

---

## 🔧 Installation
Follow these steps to set up the project:

### 1️⃣ Clone the Repository
\`\`\`
git clone https://github.com/amansatya/JARVIS-VIRTUAL-ASSISTANT.git
cd JARVIS-VIRTUAL-ASSISTANT
\`\`\`

### 2️⃣ Install Dependencies
pip install speechrecognition google-generativeai gtts pygame requests pyttsx3

### 3️⃣ Set Up Google Gemini API
- Go to **[Google AI Studio](https://aistudio.google.com/)**.
- Get your **API Key** and replace it in \`main.py\`:
\`\`\`python
genai.configure(api_key="YOUR_GEMINI_API_KEY")
\`\`\`

### 4️⃣ Run the Virtual Assistant
\`\`\`
python main.py
\`\`\`

---

## 🏗️ Usage
1. Start \`main.py\`, and JARVIS will **initialize**.
2. Say **"Jarvis"** to activate it.
3. Speak a **command**, and JARVIS will process it.
4. It will **respond via voice and text**.

---

## 🗂️ Commands
| **Command**        | **Action** |
|--------------------|-----------|
| \`open google\`     | Opens Google in browser. |
| \`open youtube\`    | Opens YouTube in browser. |
| \`open instagram\`  | Opens Instagram. |
| \`open linkedin\`   | Opens LinkedIn. |
| \`open github\`     | Opens GitHub. |
| \`play [song]\`     | Plays a predefined song from YouTube. |
| \`news\`            | Reads top 5 news headlines. |
| \`who is Elon Musk?\` | Asks Gemini AI for an answer. |

---

## 🎬 Demo Video
To add a **demo video** showing JARVIS in action:
1. Record a **screen recording**.
2. Upload it to **YouTube**.
3. Embed it here:
\`\`\`md
[![Watch the demo](https://img.youtube.com/vi/kR6L11LqDBA/0.jpg)](https://youtu.be/kR6L11LqDBA)
\`\`\`
4. Replace \`YOUR_VIDEO_ID\` with your **YouTube video ID**.

---

## 🤝 Contributing
Contributions are welcome! To contribute:
1. **Fork** the repo.
2. Create a **new branch** (\`feature-xyz\`).
3. **Commit changes** and push.
4. Submit a **Pull Request**.

---

## 📜 License
This project is **open-source**.

---

🚀 **Now, Jarvis is ready to assist you!** 🎙️
