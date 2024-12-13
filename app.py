from flask import Flask, render_template
import personal_calendars
import test_cases
from datetime import date, timedelta

app = Flask(__name__)

calendar_days_to_build = 7
start_date = test_cases.TEST_date

personal_calendar = personal_calendars.calendars(test_cases.TEST_events, start_date)
outgoings, to_dos = personal_calendar.create_calendars(start_date, calendar_days_to_build=calendar_days_to_build)

combo_calendar = {}
dates = [(start_date + timedelta(days=i)) for i in range(calendar_days_to_build)]

for date in dates:

    if date in outgoings.keys():
        outgoing = outgoings[date]
    else:
        outgoing = 0

    if date in to_dos.keys():
        todo = "\n".join(to_dos[date])
    else:
        todo = "None scheduled \n"

    combo_calendar[date.strftime("%a %d %m")] = {
f"""
"To Do:
{todo}
"Scheduled Payments: {outgoing}
"""}




@app.route('/')

def show_calendar():
    
    return render_template('calendar_template.html', data=combo_calendar)

