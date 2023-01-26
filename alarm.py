import datetime
import pyttsx3
import pytz


def alarm(time):
    engine = pyttsx3.init()
    d = datetime.date.today()
    day = d.isoweekday()
    alarm_on = True
    if 1 <= day <= 5:
        is_weekday = True
    else:
        is_weekday = False
    new_time = time.split(':')
    new_hour = int(new_time[0])
    new_minute = int(new_time[1])
    while alarm_on and is_weekday:
        try:
            t = datetime.datetime.now(tz=pytz.UTC)
            t_here = t.astimezone(pytz.timezone('Us/Central'))
            if t_here.hour == new_hour and t_here.minute == new_minute:
                print('alarm')
                engine.say(f"Good morning Max. Today is {t.strftime('%A %B %d')}.")
                engine.runAndWait()
                alarm_on = False
        except:
            pass


