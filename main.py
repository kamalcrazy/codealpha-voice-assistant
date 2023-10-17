import speech_recognition as sr
from gtts import gTTS
import pygame
import os
pygame.init()
r = sr.Recognizer()
def speak(text):
    tts = gTTS(text)
    tts.save("output.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Main assistant function
def assistant():
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        try:
            user_input = r.recognize_google(audio)
            print("You said: " + user_input)
            response = "I heard you say " + user_input
            speak(response)

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand your audio.")
        except sr.RequestError as e:
            print(f"Sorry, there was an error with the request: {e}")
if __name__ == "__main__":
    print("Starting your custom voice assistant...")
    assistant()
