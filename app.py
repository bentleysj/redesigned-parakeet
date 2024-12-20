from flask import Flask, render_template
import personal_calendars
import test_cases
from datetime import date, timedelta

app = Flask(__name__)

calendar_days_to_build = 30
start_date = test_cases.TEST_date

personal_calendar = personal_calendars.calendars(test_cases.TEST_events, start_date)
calendars  = personal_calendar.create_calendars(calendar_days_to_build=calendar_days_to_build)
to_dos, outgoings, total_outgoings = personal_calendar.create_output_calendar(calendars)

current_todos = personal_calendar.update_current_tasks(to_dos)
                 
    
@app.route('/')

def show_calendar():
    
    return render_template('calendar_template.html', to_dos=to_dos , total_outgoings=total_outgoings,  outgoing=outgoings)

def current_tasks():
    
    
    
    return current_todos

