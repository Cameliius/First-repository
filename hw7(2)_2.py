import speech_recognition as sr
# import pyaudio
import random

rec = sr.Recognizer()

hi = ['Приветик!', 'Хай!', 'И тебе привет, как день?', 'Привет ;)']
greeting = random.choice(hi)

films = ['Дивергент', 'Аватар', 'Я робот', 'Последний богатырь', 'Матрица', 'Гарри Поттер']
use_film = random.choice(films)


with sr.Microphone(device_index=1) as source:
    print('Скажите что-нибудь...')
    audio = rec.listen(source)
text = rec.recognize_google(audio, language='ru_RU').lower()
print('Вы сказали: ', text)
if text == "привет":
    print(greeting)

elif text == "фильм":
    print(use_film)