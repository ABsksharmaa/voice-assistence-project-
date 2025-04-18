import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Speak function
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Listen function
def listen():
    try:
        with sr.Microphone() as source:
            print("🎤 Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(f"User said: {command}")
            return command
    except:
        return "Sorry, I didn't get that."

# Main
talk("Hello! I'm your assistant. What can I do for you?")
command = listen()
talk(f"You said: {command}")
