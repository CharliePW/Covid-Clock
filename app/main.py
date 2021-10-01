"""this module is the app"""

from flask import Flask, request, render_template, redirect, Markup
from news_filter import get_news
from new_cases_today import get_data
from weather_update import get_weather
import pyttsx3
import sched
import time_conversions
import time
import logging

#setting constants and global variables
s = sched.scheduler(time.time, time.sleep)
logging.basicConfig(filename='sys.log', encoding='utf-8', level=logging.DEBUG)
app = Flask(__name__)
engine = pyttsx3.init()
notifications = []
alarms = []
#alarm_notif = {"title":"This is an alarm notification", "content": ""}


def announce(announcement : str) -> None :
    """this function does text to speech"""
    try:
        engine.endLoop()
    except:
        logging.error('PyTTSx3 Endloop error')
    engine.say(announcement)
    engine.runAndWait()

@app.route('/index')
def schedule_event():
    """this functions returns the template of the app

    it handles setting/removing alarms and notifications"""


    global alarms
    global notifications
    global alarm_notif

    s.run(blocking=False)

    alarm_time = request.args.get("alarm")
    input = request.args.get("two")
    alarm_notif = {"title":"This is an alarm notification", "content": ""}

    #setting an alarm
    if alarm_time:
        alarm_dict = {"title":"","content":""}
        alarm_dict.update({"title": input})
        alarm_dict.update({"content": alarm_time})
        alarms.append(alarm_dict)
        current_time = time_conversions.current_time_hhmm()
        alarm_time = str(alarm_time[-5::])
        print("alarm_time: ",alarm_time)
        delay = time_conversions.hhmm_to_seconds(alarm_time) - time_conversions.hhmm_to_seconds(current_time)
        print("delay: ", delay)
        e1 = s.enterabs(delay, 1, announce, ["ALARM",])
        e2 = s.enterabs(delay, 1, print, ["alarm alarm alarm",])
        alarm_notif_content = "The alarm " + str(alarms[-1]["title"]) + " will go off at:" + alarm_time
        alarm_notif.update({"content":alarm_notif_content})
        notifications.insert(0, alarm_notif)

    #setting a default notification which are the local covid cases
    if len(notifications) == 0:
        covid_data_dict = get_data()
        notifications = [covid_data_dict]
        announce(notifications[0]["content"])

    #get weather data
    weather_checkbox = request.args.get("weather")
    if weather_checkbox:
        notifications.insert(0, get_weather())
        announce(notifications[0]["content"])

    #adding news notifications
    news_checkbox = request.args.get("news")
    if news_checkbox:
        news_list = get_news()
        if len(notifications) <= len(news_list) + 2:
            index = 1
            for item in news_list:
                url = item["content"]
                content = Markup('<a href="{}">Click here</a>'.format(url))
                item.update({"content":content})
                notifications.append(item)
            announce(news_list[0]["title"])

    #removing notifications
    remove_notif = request.args.get("notif")
    if remove_notif:
        for item in notifications:
            if item["title"] == remove_notif:
                notifications.remove(item)
                e4 = s.enterabs(1, 1, print, ["the notification is removed",])

    #removing alarms
    remove_alarm = request.args.get("alarm_item")
    if remove_alarm:
        for alarm in alarms:
            if alarm["title"] == remove_alarm:
                alarms.remove(alarm)
                e5 = s.enterabs(1, 1, print, ["the alarm is removed",])


    return render_template("CA3_template.html", alarms = alarms, notifications = notifications, title = "Covid CLock", image = "COVID.jpg")

@app.route("/")
def go_to_index():
    """this function just redirects to '/index' """
    return redirect("/index")

if __name__ == "__main__":
    app.run()
