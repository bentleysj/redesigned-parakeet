from flask import Flask, render_template
import personal_calendars
import test_cases
from datetime import date, timedelta

app = Flask(__name__)

calendar_days_to_build = 30
start_date = test_cases.TEST_date

personal_calendar = personal_calendars.calendars(test_cases.TEST_events, start_date)
to_dos, outgoings, total_outgoings = personal_calendar.create_output_calendar(personal_calendar.create_calendars(calendar_days_to_build=calendar_days_to_build))

current_todos = personal_calendar.update_current_tasks(to_dos)

# ren_personal_calendar = {}
# ren_outgoing_calendar = {}
# ren_total_outgoing_calendar = {}
# dates = [(start_date + timedelta(days=i)) for i in range(calendar_days_to_build)]

# for date in dates:

#     if date in total_outgoings.keys():
#         total_outgoing = total_outgoings[date]
#     else:
#         total_outgoing = 0

#     if date in to_dos.keys():
#         todo = to_dos[date]
#     else:
#         todo = ["None scheduled."]

#     if date in outgoings.keys():
#         outgoing = outgoings[date]
#     else:
#         outgoing = ["None scheduled."]

#     ren_personal_calendar[date.strftime("%a %d %m")] =  todo
#     ren_outgoing_calendar[date.strftime("%a %d %m")] =  outgoing
#     ren_total_outgoing_calendar[date.strftime("%a %d %m")] =  total_outgoing
                   
    
@app.route('/')

def show_calendar():
    
    return render_template('calendar_template.html', to_dos=to_dos , total_outgoings=total_outgoings,  outgoing=outgoings)

def current_tasks():
    
    
    
    return current_todos

