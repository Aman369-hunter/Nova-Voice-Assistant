import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import pygame
import os
from gtts import gTTS
from openai import OpenAI

# -----------------------------
# API KEYS
# -----------------------------

NEWS_API_KEY = "your_api_key_here"
OPENAI_API_KEY = "your_api_key_here"
client = OpenAI(api_key=OPENAI_API_KEY)

# -----------------------------
# MUSIC LIBRARY
# -----------------------------

musicLibrary = {
    "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc",
    "shape of you": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
    "faded": "https://www.youtube.com/watch?v=60ItHLz5WEA",
    "balenci" : "https://www.youtube.com/watch?v=siw7-MTgE4s&list=RDsiw7-MTgE4s&start_radio=1"
}

# -----------------------------
# TEXT TO SPEECH
# -----------------------------

engine = pyttsx3.init()

def speak(text):
    print("nova:", text)
    engine.say(text)
    engine.runAndWait()


# -----------------------------
# SPEECH RECOGNITION
# -----------------------------

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            command = command.lower()
            print("User:", command)
            return command

        except sr.UnknownValueError:
            return ""

# -----------------------------
# OPENAI RESPONSE
# -----------------------------

def ask_ai(question):
    try:

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role":"system","content":"You are nova, a helpful AI assistant."},
                {"role":"user","content":question}
            ]
        )

        reply = response.choices[0].message.content
        return reply
    
    except Exception as e:
        return "Sorry! AI assistant is not available right now"

# -----------------------------
# GET NEWS
# -----------------------------

def get_news():

    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"

    response = requests.get(url)
    data = response.json()

    articles = data["articles"][:5]

    speak("Here are the top news headlines")

    for i, article in enumerate(articles):
        speak(f"News {i+1}")
        speak(article["title"])

# -----------------------------
# COMMAND PROCESSOR
# -----------------------------

def process_command(command):

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")

    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")

    elif "play" in command:

        song = command.replace("play","").strip()

        if song in musicLibrary:
            speak(f"Playing {song}")
            webbrowser.open(musicLibrary[song])

        else:
            speak("Song not found")

    elif "news" in command:
        get_news()

    elif "exit" in command or "stop" in command:
        speak("Goodbye")
        exit()

    else:
        speak("Let me think")

        reply = ask_ai(command)

        speak(reply)

# -----------------------------
# MAIN PROGRAM
# -----------------------------

def main():

    speak("Initializing nova")

    while True:

        print("Waiting for wake word...")

        word = listen()

        if "nova" in word:

            speak("Yes")

            command = listen()

            process_command(command)

# -----------------------------
# RUN PROGRAM
# -----------------------------

if __name__ == "__main__":
    main()