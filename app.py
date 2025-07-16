import speech_recognition as sr
import pyttsx3
import os
import re
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

# --- CONFIGURATION ---
API_KEY = "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"
MODEL_NAME = "llama3-70b-8192"
CODE_FILE = "generated_code.py"
LAUNCH_VSCODE = True

# --- SETUP ---
tts_engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    print("🗣️ Speaking:", text)
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen_command():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        speak("Tell me what Python code you want me to write.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"🧾 You said: {text}")
            return text
        except sr.UnknownValueError:
            print("❌ Could not understand audio.")
        except sr.RequestError as e:
            print(f"❌ Speech Recognition error: {e}")
    return None

def get_input():
    print("\n🔘 Choose input method:")
    print("1. Voice input")
    print("2. Text input")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        voice_text = listen_command()
        if voice_text:
            return voice_text
        else:
            speak("Voice input failed. Please type your request.")
            return input("✍️ Enter your Python code request: ")
    else:
        return input("✍️ Enter your Python code request: ")

def generate_code_with_llm(prompt_text):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful Python code generator. Generate clean Python code in a single block and give a short explanation."),
        ("user", prompt_text)
    ])

    llm = ChatGroq(
        temperature=0,
        groq_api_key=API_KEY,
        model_name=MODEL_NAME
    )

    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    return chain.invoke({"query": prompt_text})

def extract_code_and_explanation(response):
    # Extract all code blocks from triple backticks
    code_blocks = re.findall(r"```(?:python)?\s*(.*?)```", response, re.DOTALL)
    all_code = "\n".join(code_blocks).strip()

    # Remove all code blocks to leave only the explanation
    explanation = re.sub(r"```(?:python)?\s*.*?```", "", response, flags=re.DOTALL).strip()

    return all_code, explanation

def write_code_to_file(code):
    if code:
        with open(CODE_FILE, "a") as f:
            f.write(f"\n{code}\n")
        print(f"✅ Code written to {CODE_FILE}")
        speak("Your complete Python code has been written.")
        if LAUNCH_VSCODE:
            os.system(f"code {CODE_FILE}")
    else:
        speak("No valid Python code found to write.")

def run_generated_code():
    if os.path.exists(CODE_FILE):
        speak("Running the generated Python code.")
        print("🚀 Running the code...\n")
        os.system(f"python {CODE_FILE}")
    else:
        speak("No code file found to run.")
        print("❌ No generated_code.py file found.")

def main():
    while True:
        command = get_input()

        if command and command.strip().lower() == "run":
            run_generated_code()
            continue

        if command:
            response = generate_code_with_llm(command)
            print("\n🧠 Raw LLM Output:\n", response)

            code, explanation = extract_code_and_explanation(response)

            if explanation:
                print("\n📚 Explanation:\n", explanation)
                speak(explanation)

            if code:
                print("\n💻 Clean Python Code:\n", code)
                write_code_to_file(code)
        else:
            speak("No input provided. Exiting.")
            break

if __name__ == "__main__":
    main()
