import datetime

from bfunctions import take_command, talk
from alarm import alarm
import pyttsx3 as tts


engine = tts.init()


def run():
    command = take_command()
    running = True
    if 'set an alarm at' in command:
        time = command[-5:]
        print(time)
        alarm(time)
    elif 'what is the time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'goodbye' in command:
        talk('Goodbye Max')
        running = False
    else:
        talk("I didn't quite get that")
    return running


while run():
    try:
        run()
    except:
        pass
