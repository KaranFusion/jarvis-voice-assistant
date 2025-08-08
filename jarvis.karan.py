import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser

# Initialize text-to-speech
engine = pyttsx3.init()

def speak(audio):
    """Speak the given text."""
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    """Greet the user based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning, Karan!")
    elif 12 <= hour < 18:
        speak("Good Afternoon, Karan!")
    else:
        speak("Good Evening, Karan!")
    speak("I am Jarvis. How can I help you?")

def take_command():
    """Listen for user commands and return them as text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        try:
            audio = recognizer.listen(source)
            print("Recognizing...")
            command = recognizer.recognize_google(audio, language='en-in')
            print(f"You said: {command}")
        except Exception as e:
            print("Say that again please...")
            return None
        return command.lower()

def execute_command(command):
    """Perform tasks based on the user's command."""
    if 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")
    elif 'open google' in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {current_time}")
    elif 'open notepad' in command:
        speak("Opening Notepad")
        os.system("notepad")
    elif 'exit' in command or 'quit' in command:
        speak("Goodbye, Karan!")
        exit()
    else:
        speak("I'm not sure how to do that yet!")

if __name__ == "__main__":
    wish_me()
    while True:
        command = take_command()
        if command:
            execute_command(command)
