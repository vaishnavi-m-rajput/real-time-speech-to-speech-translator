<h1 align="center">🗣️🎙️ Real-Time Speech-to-Speech Translator</h1>
<br>

<div align="center">
  <img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmhnYzNrejlrbXRwYXhjbHU1ZjVpbWg3NzVxOTQ1azBpdmJudmdpMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/aeqpymkqoW3BAiqboo/giphy.gif"/>
</div>

<br>

## 🧠 About the Project

**Real-Time Speech Translator** is a lightweight, offline-capable tool designed to:  
🎤 Recognize speech from a microphone,  
🌐 Translate it between multiple languages, and  
🔊 Speak out the translated result — all in *real time*.

Perfect for:
- Travelers ✈️  
- Language learners 📚  
- Multilingual environments (military training, field ops, etc.) 🪖

> 🎯 Built using Python and user-friendly libraries like `speech_recognition`, `gTTS`, `deep_translator`, and `playsound`.

---

## 🚀 Features

- 🎙️ Real-time speech input  
- 🔄 Bidirectional translation:
  - English ↔ Hindi  
  - English ↔ Tamil  
  - English ↔ Telugu  
- 📢 Speech output in target language  
- 🧠 Smart language pair selection  
- 💬 Natural, human-sounding speech using Google Text-to-Speech  
- 🔌 Offline-friendly (once dependencies are installed)

---

## 🖼️ Demo Preview

| Speak | Translates | Speaks Back |
|------|------------|-------------|
| ![Mic](https://img.icons8.com/color/96/microphone--v1.png) | ![Translate](https://img.icons8.com/color/96/google-translate.png) | ![Speaker](https://img.icons8.com/color/96/speaker.png) |

---

## 📂 Directory Structure

```
📁 speech-translator/
│
├── translator.py       # Main Python script
├── README.md           # This file 
└── requirements.txt    # List of dependencies
```

---

## ⚙️ Installation

First, make sure Python 3.x is installed.

### 1. Clone this repo:

```bash
git clone https://github.com/vaishnavi-m-rajput/real-time-speech-to-speech-translator.git
cd speech-translator
```

### 2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate    # for macOS/Linux
venv\Scripts\activate       # for Windows
```

### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, install manually:

```bash
pip install SpeechRecognition
pip install deep-translator
pip install gTTS
pip install playsound
```

---

## 🛠️ Usage

Run the Python script:

```bash
python translator.py
```

- Select your preferred language pair.  
- Start speaking when prompted.  
- Say **“exit”** to stop the program.

---

## 🎧 How It Works

1. **Listen** to voice input using `speech_recognition`  
2. **Convert speech to text** via Google’s recognizer  
3. **Translate** using `deep_translator`  
4. **Text-to-speech output** via `gTTS`  
5. **Playback** using `playsound`

---

## 🌍 Supported Languages

| Source | Target |
|--------|--------|
| English | Hindi |
| Hindi   | English |
| English | Tamil |
| Tamil   | English |
| English | Telugu |
| Telugu  | English |

> You can add more languages by updating the language codes in the code 💻✨

---

## 🔐 Permissions

Allow microphone access when prompted by your OS.  
(Windows, macOS, Linux – all supported)

---

## 📷 Screenshots

<img width="1920" height="1030" alt="image" src="https://github.com/user-attachments/assets/97b77c9c-5bd3-4f5a-af33-b34c52b65921" />


---

## 📚 References

- [Google Text-to-Speech (gTTS)](https://pypi.org/project/gTTS/)  
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)  
- [Deep Translator](https://pypi.org/project/deep-translator/)  
- [Playsound](https://pypi.org/project/playsound/)

---

## ❤️ Future Enhancements

- Add GUI with Streamlit or Tkinter  
- Add full offline translation using transformer models  
- Improve voice output with pyttsx3  
- Add support for audio file input

---

## 🙋‍♀️ Author

Made with 💕 by **Vaishnavi**  
*Passionate about voice tech, AI, and making ideas speak — literally.* 

Connect with me on [LinkedIn](https://www.linkedin.com/in/vaishnavi-rajput-2144b1255/)

---

## 🧾 License

MIT License — use it freely, respectfully, and with credit!

---

