import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set female voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Speech speed
engine.setProperty('rate', 170)


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        command = command.lower()
        print("You said:", command)
        return command

    except sr.UnknownValueError:
        speak("Sorry, I could not understand.")
        return ""

    except sr.RequestError:
        speak("Network error.")
        return ""


# Start assistant
speak("Hello Sayali. I am your personal voice assistant.")

while True:

    command = listen()

    if "hello" in command or "hi" in command:
        speak("Hello Sayali, how can I help you?")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "search" in command:
        speak("Searching on Google")
        webbrowser.open("https://www.google.com/search?q=" + command)

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak("The time is " + current_time)

    elif "stop assistant" in command or "exit" in command:
        speak("Goodbye Sayali")
        break

    elif command != "":
        speak("You said " + command)