import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
import google.generativeai as genai
from gtts import gTTS
import pygame
import os
from dotenv import load_dotenv

recognizer = sr.Recognizer()
engine = pyttsx3.init()
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)


def speak_old(text):
    engine.say(text)
    engine.runAndWait()


def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")


def aiProcess(c):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Correct model name
        # Limit response length for short answers
        response = model.generate_content(
            c,
            stream=True,
            generation_config={"max_output_tokens": 50}  # Limits response length
        )
        full_response = ""
        for chunk in response:
            if chunk.text:
                print(chunk.text, end="", flush=True)  # Print chunk immediately
                speak(chunk.text)  # Speak each chunk in real-time
                full_response += chunk.text

        print("\n")  # Ensure proper formatting in the console
        return full_response if full_response else "Sorry, I couldn't process that."

    except Exception as ex:
        print(f"Error in AI processing: {ex}")  # Print error for debugging
        return "There was an error processing your request."


def process(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        re = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}")
        if re.status_code == 200:
            data = re.json()
            if data["status"] == "ok" and "articles" in data:
                articles = data["articles"]
                if len(articles) == 0:
                    speak("No news articles found at the moment.")
                else:
                    # Get top 5 headlines
                    for i, article in enumerate(articles[:5], 1):
                        speak(f"News {i}:{article['title']}")
            else:
                speak("There was an issue retrieving the news.")
        else:
            speak(f"Failed to fetch news. Status Code: {re.status_code}")
    else:
        # Let OpenAI handle the request
        output = aiProcess(c)
        speak(output)
        pass


if __name__ == '__main__':
    speak("INITIALIZING JARVIS A VIRTUAL ASSISTANT")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()

        try:
            with sr.Microphone() as source:
                print("LISTENING...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("WELCOME")
                # Listen for command
                with sr.Microphone() as source:
                    print("JARVIS ACTIVE...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    command = r.recognize_google(audio)
                    process(command)
        except Exception as e:
            print("Error; {0}".format(e))
