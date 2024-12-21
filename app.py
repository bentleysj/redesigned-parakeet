from flask import Flask, render_template
import personal_calendars
import test_cases
from datetime import date, timedelta

app = Flask(__name__)


# TEST BLOCK
calendar_days_to_build = 7
start_date = date.today() #test_cases.TEST_date
events = test_cases.TEST_events
current_tasks = test_cases.TEST_outstanding_actions


personal_calendar = personal_calendars.calendars(events, current_tasks, start_date)
personal_calendar.create_calendars(calendar_days_to_build=calendar_days_to_build)
personal_calendar.update_current_tasks(start_date)
personal_calendar.create_output_daily_task()
to_dos, outgoings, total_outgoings = personal_calendar.create_output_calendar()


current_todos = personal_calendar.current_to_do_list

@app.route('/')

def user_home():
  
    return render_template('user-home.html', to_dos=to_dos , total_outgoings=total_outgoings,  outgoing=outgoings, current_todos=current_todos)
    
@app.route('/calendar')

def show_calendar():
  
    return render_template('calendar_template.html', to_dos=to_dos , total_outgoings=total_outgoings,  outgoing=outgoings)

@app.route('/today')

def current_tasks():    
    
    return render_template('current_tasks.html', current_todos=current_todos)

