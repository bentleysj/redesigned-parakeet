from flask import Flask, render_template
import personal_calendars
import test_cases
from datetime import date, timedelta

app = Flask(__name__)

calendar_days_to_build = 7
start_date = test_cases.TEST_date

personal_calendar = personal_calendars.calendars(test_cases.TEST_events, start_date)
total_outgoings, to_dos, outgoings = personal_calendar.create_calendars(start_date, calendar_days_to_build=calendar_days_to_build)

ren_personal_calendar = {}
ren_outgoing_calendar = {}
ren_total_outgoing_calendar = {}
dates = [(start_date + timedelta(days=i)) for i in range(calendar_days_to_build)]

for date in dates:

    if date in total_outgoings.keys():
        total_outgoings = total_outgoings[date]
    else:
        total_outgoings = 0

    if date in to_dos.keys():
        # todo = "\n".join(to_dos[date])
        todo = to_dos[date]
    else:
        todo = "None scheduled \n"

    if date in outgoings.keys():
        # todo = "\n".join(to_dos[date])
        outgoings = outgoings[date]
    else:
        outgoings = "None scheduled \n"

    ren_personal_calendar[date.strftime("%a %d %m")] =  todo
    ren_total_outgoing_calendar[date.strftime("%a %d %m")] =  total_outgoings
                   
    
@app.route('/')

def show_calendar():
    
    return render_template('calendar_template.html', to_dos=ren_personal_calendar, toal_outgoing=ren_total_outgoing_calendar,  outgoing=ren_outgoing_calendar)

