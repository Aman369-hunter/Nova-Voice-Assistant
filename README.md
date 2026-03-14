# Nova-Voice-Assistant

# NOVA AI – Voice Activated Virtual Assistant

NOVA AI is a Python-based voice activated virtual assistant capable of performing tasks such as opening websites, playing music, fetching news, and answering questions using artificial intelligence.

The assistant listens for the wake word **"Nova"**, processes voice commands, and responds with speech.

This project demonstrates the integration of speech recognition, automation, and AI using Python.

---

## Features

### Voice Recognition
The assistant listens to the user through the microphone using the SpeechRecognition library and activates when it hears the wake word **"Nova"**.

### Text to Speech
NOVA converts text responses into speech using the pyttsx3 library to provide voice feedback.

### Web Browsing
The assistant can open popular websites including:

- Google
- YouTube
- Facebook
- LinkedIn

### Music Playback
NOVA can play songs from a predefined music library by opening the corresponding YouTube links.

### News Fetching
Latest news headlines are retrieved using the NewsAPI service and read aloud to the user.

### AI Responses
For general questions, NOVA uses the OpenAI API to generate intelligent responses.

---

## Technologies Used

- Python
- SpeechRecognition
- pyttsx3
- requests
- pygame
- gTTS
- OpenAI API
- webbrowser module

---

## Example Commands

Wake word:

Nova

Commands you can try:

Open Google  
Open YouTube  
Play Believer  
Tell me the news  
What is Artificial Intelligence  

---

## Installation

Clone the repository
