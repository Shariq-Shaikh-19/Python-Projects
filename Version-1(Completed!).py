import speech_recognition as sr
import webbrowser
import pyttsx3
import pywhatkit
from datetime import datetime

r = sr.Recognizer()
engine = pyttsx3.init("sapi5")

def speak(text):
    engine.say(text)
    engine.runAndWait()     
    
def open_website(website):
    webbrowser.open(f"http://www.{website}.com")

def play_songs(songs):
    pywhatkit.playonyt(songs)

def tell_time(current_time):
    speak(f"The time is {current_time}")
    
if __name__ == "__main__":
    speak("Initializing Jarvis...")

    with sr.Microphone() as source:
        print("Calibrating microphone...")
        r.adjust_for_ambient_noise(source, duration=1)

    print("Ready.")

    # Listen for the wake word "Jarvis"
    # obtain audio from the microphone

    try:

        while True:

            try:

                with sr.Microphone() as source:
                    audio = r.listen(source, timeout=2, phrase_time_limit=1)

                command = r.recognize_google(audio).lower()
                print("Recognized:", command)
                print("Command:", command)

                if "jarvis" in command:
                    print("Wake word detected!")
                    speak("Yes sir?")
                    
                    while True:
                        with sr.Microphone() as source:
                            print("Jarvis Active")
                            audio = r.listen(source, timeout=3, phrase_time_limit=5)
                        command = r.recognize_google(audio).lower()
                    
                        words = command.split()

                        if "open" in words:
                            print("Open command detected")
                            position = words.index("open")
                            if position + 1 < len(words):
                                website = words[position + 1:]
                                website = " ".join(website)
                                open_website(website)
                            else:
                                speak("Please tell me which website to open.")

                        elif "play" in words:
                            name_song = words.index("play")
                            
                            if name_song + 1 < len(words):
                                songs = words[name_song + 1:]
                                songs = " ".join(songs)
                                play_songs(songs)
                            else:
                                speak("Please tell me which song to play.")

                        elif "time" in words:
                            now = datetime.now()
                            current_time = now.strftime("%I:%M %p")
                            tell_time(current_time)


                        elif "exit" in words:
                            speak("Going back to sleep.")
                            break

            except sr.UnknownValueError:
                continue
            except sr.WaitTimeoutError:
                continue         


    except Exception as e:
        print(type(e))
        print(e)