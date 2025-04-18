import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import pyjokes
import openai

# Set your OpenAI API Key
openai.api_key = "enter your api .......yes"

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

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

def chatgpt_response(command):
    response = openai.Completion.create(
        engine="text-davinci-003",  #  can use other models too like gpt-3.5
        prompt=command,
        max_tokens=100
    )
    return response.choices[0].text.strip()

def run_assistant():
    talk("Hi, I am your assistant. How can I help you?")
    command = listen()

    if "wwe" in command:
        talk("Opening WWE")
        webbrowser.open("https://www.wwe.com")
    
    elif "youtube" in command:
        talk("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "google" in command:
        talk("Opening Google")
        webbrowser.open("https://google.com")

    elif "what is" in command:
        topic = command.replace("what is", "")
        info = wikipedia.summary(topic, sentences=2)
        print(info)
        talk(info)

    elif "joke" in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif "chat" in command:  # Adding ChatGPT response
        talk("Sure, let me answer your question.")
        answer = chatgpt_response(command)
        print(answer)
        talk(answer)

    else:
        talk("Sorry, I didn't understand that.")
        

run_assistant()
