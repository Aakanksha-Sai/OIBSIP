import speech_recognition as sr
from gtts import gTTS
import os

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Define your basic voice assistant function
def basic_voice_assistant():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")

            if "hello" in command.lower():
                response = "Hello! How can I help you today?"
            elif "time" in command.lower():
                import datetime
                now = datetime.datetime.now()
                response = f"The current time is {now.strftime('%H:%M')}"
            elif "date" in command.lower():
                import datetime
                now = datetime.datetime.now()
                response = f"Today is {now.strftime('%A, %B %d, %Y')}"
            else:
                response = "I'm sorry, I didn't understand your command."

            print(response)
            tts = gTTS(text=response, lang='en')
            tts.save("response.mp3")
            os.system("mpg321 response.mp3")

    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")

# Call the basic voice assistant function
basic_voice_assistant()
