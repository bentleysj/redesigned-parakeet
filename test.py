import personal_calendars
import test_cases
from datetime import date

calendar_days_to_build = 14
start_date = date.today()

personal_calendar = personal_calendars.calendars(test_cases.TEST_events, start_date)
# total_outgoings, to_dos, outgoings = personal_calendar.create_calendars(calendar_days_to_build)

total_outgoings, to_dos, outgoings = personal_calendar.create_output_calendar(personal_calendar.create_calendars(calendar_days_to_build=calendar_days_to_build))

current_tasks = personal_calendar.update_current_tasks(test_cases.TEST_outstanding_actions)

assert len(total_outgoings) == 14
assert len(to_dos) == 14
assert len(outgoings) == 14

