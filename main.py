import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

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

if __name__ == '__main__':
    speak("INITIALIZING JARVIS A VIRTUAL ASSISTANT")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()

        print("RECOGNIZING...")
        try:
            with sr.Microphone() as source:
                print("LISTENING...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("YA")
                # Listen for command
                with sr.Microphone() as source:
                    print("JARVIS ACTIVE...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    command = r.recognize_google(audio)

                    process(command)
        except Exception as e:
            print("Error; {0}".format(e))