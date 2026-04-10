from deep_translator import GoogleTranslator
from gtts import gTTS
import pygame
import os

# Input text
text = input("Enter English text: ")

# Translate English → Kannada
translated = GoogleTranslator(source='en', target='kn').translate(text)

print("Kannada Translation:", translated)

# Convert text to speech
tts = gTTS(text=translated, lang='kn')
tts.save("kannada_audio.mp3")

# Play audio
pygame.mixer.init()
pygame.mixer.music.load("kannada_audio.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue
