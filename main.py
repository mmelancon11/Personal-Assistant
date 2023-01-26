import speech_recognition as sr
import pyttsx3 as tts
from alarm import alarm

listener = sr.Recognizer()
engine = tts.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run():
    command = take_command()
    print(command)


alarm_time = input('>')

alarm(alarm_time)