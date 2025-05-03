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
load_dotenv()
newsapi = os.getenv("NEWS_API_KEY")
genai_api_key = os.getenv("GENAI_API_KEY")
genai.configure(api_key=genai_api_key)
recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")
def aiProcess(c):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        response = model.generate_content(
            c, stream=True, generation_config={"max_output_tokens": 50}
        )
        full_response = ""
        for chunk in response:
            if chunk.text:
                print(chunk.text, end="", flush=True)
                speak(chunk.text)
                full_response += chunk.text
        print("\n")
        return full_response if full_response else "Sorry, I couldn't process that."
    except Exception as ex:
        print(f"Error in AI processing: {ex}")
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
        song = c.lower().split(" ", 1)[1]
        link = musiclibrary.music.get(song, None)
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, I couldn't find that song.")
    elif "news" in c.lower():
        re = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if re.status_code == 200:
            data = re.json()
            if data["status"] == "ok" and "articles" in data:
                articles = data["articles"]
                if len(articles) == 0:
                    speak("No news articles found at the moment.")
                else:
                    for i, article in enumerate(articles[:5], 1):
                        speak(f"News {i}: {article['title']}")
            else:
                speak("There was an issue retrieving the news.")
        else:
            speak(f"Failed to fetch news. Status Code: {re.status_code}")
    else:
        output = aiProcess(c)
        speak(output)
if __name__ == '__main__':
    speak("INITIALIZING JARVIS A VIRTUAL ASSISTANT")
    while True:
        try:
            with sr.Microphone() as source:
                print("LISTENING FOR WAKE WORD...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                try:
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    word = recognizer.recognize_google(audio)
                    print(f"Heard: {word}")
                    if "jarvis" in word.lower():
                        speak("WELCOME")
                        with sr.Microphone() as source:
                            print("JARVIS ACTIVE, LISTENING FOR COMMAND...")
                            recognizer.adjust_for_ambient_noise(source, duration=1)
                            try:
                                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                                command = recognizer.recognize_google(audio)
                                print(f"Command: {command}")
                                process(command)
                            except sr.UnknownValueError:
                                print("Sorry, I couldn't understand the command.")
                                speak("Sorry, I couldn't understand the command.")
                            except sr.WaitTimeoutError:
                                print("Timeout: No command detected.")
                                speak("I didn't hear any command.")
                except sr.WaitTimeoutError:
                    print("Timeout: No wake word detected.")
                except sr.UnknownValueError:
                    print("Wake word not recognized.")
                except sr.RequestError as e:
                    print(f"Speech recognition service error: {e}")
        except Exception as e:
            print(f"Error: {e}")