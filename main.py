from gtts import gTTS
from discord import Webhook, RequestsWebhookAdapter
import requests
import os
import time
import speech_recognition as sr
import playsound

def speak(text):
    tts = gTTS(text=text,lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove("voice.mp3")

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            speak(said)
            return said
        except Exception as e:
            print(e)

webhook = Webhook.from_url("Enter_Webhook_Url_here", adapter=RequestsWebhookAdapter())
#webhook.send("Hi")
speak("Listening")
text = get_audio()
webhook.send(text)