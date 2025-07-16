# 🧠 Voice-Driven Python Code Generator with LangChain + Groq

![Voice Python Assistant](voice_codeagent/Screenshot 2025-07-16 110917.png)

This project is a **voice-activated Python code generator and executor** that uses the **Groq API with LLaMA 3**, **LangChain**, **SpeechRecognition**, and **Text-to-Speech (TTS)** to provide an interactive AI coding assistant.

---

## ✨ Features

- 🎙️ **Voice or Text Input**: Interact with the assistant by speaking or typing.
- 🧠 **AI-Powered Code Generation**: Uses Groq LLaMA 3 model to generate clean Python code with explanation.
- 💬 **Text-to-Speech Feedback**: Explains the generated code using voice.
- 💾 **Code Logging**: Appends each generated code block to `generated_code.py`.
- 💻 **VS Code Integration**: Automatically opens the file in VS Code after writing code.
- 🚀 **Voice Command Execution**: Say or type **"run"** to execute the Python code that was generated.

---

## 📁 Project Structure

voice-codeagent/
-├── main.py # Main application script
-├── generated_code.py # Output file for generated code
-│── voice_code_ai_banner.png # Image for README
-└── README.md # You're here!


## 🔧 Setup Instructions

### 1. Clone this repository

```bash
git clone https://github.com/Leelavinothan12/voice_codeagent/tree/main
cd voice-code-ai
