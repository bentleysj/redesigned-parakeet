import personal_calendars
import test_cases
from datetime import date

calendar_days_to_build = 14
start_date = date(2024, 12, 1)

personal_calendar = personal_calendars.calendars(test_cases.TEST_events, start_date)
# total_outgoings, to_dos, outgoings = personal_calendar.create_calendars(calendar_days_to_build)

to_dos, outgoings, total_outgoings = personal_calendar.create_output_calendar(personal_calendar.create_calendars(calendar_days_to_build=calendar_days_to_build))

test_key = start_date.strftime("%a %d %m")
test_key_2 = date(2024,12,2).strftime("%a %d %m")

assert len(total_outgoings) == calendar_days_to_build
assert len(to_dos) == calendar_days_to_build
assert len(outgoings) == calendar_days_to_build

assert to_dos[test_key] == ["Drink water"]
assert outgoings[test_key] == ["None Scheduled."]
assert total_outgoings[test_key] == 0

assert total_outgoings[test_key_2] == 1277 + 150.91
assert outgoings[test_key_2] == [] # get expected
assert to_dos[test_key_2] == [] # get expected

start_date = date.today()
current_tasks = personal_calendar.update_current_tasks(test_cases.TEST_outstanding_actions)

# current tasks includes new from current day and test cases outstanding.




