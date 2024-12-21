import personal_calendars
import test_cases
from datetime import date

calendar_days_to_build = 14
start_date = date(2024, 12, 1)

personal_calendar = personal_calendars.calendars(test_cases.TEST_events, test_cases.TEST_outstanding_actions,  start_date)

calendars = personal_calendar.create_calendars(calendar_days_to_build=calendar_days_to_build)
to_dos, outgoings, total_outgoings = personal_calendar.create_output_calendar()

test_key = start_date.strftime("%a %d %m")
test_key_2 = date(2024,12,2).strftime("%a %d %m")

assert len(total_outgoings) == calendar_days_to_build
assert len(to_dos) == calendar_days_to_build
assert len(outgoings) == calendar_days_to_build

assert to_dos[test_key] == ["Drink water"]
assert outgoings[test_key] == ["None Scheduled."]
assert total_outgoings[test_key] == 0



assert total_outgoings[test_key_2] == 1277 + 150.91
assert outgoings[test_key_2] == ['Mortgage : 1000', 'Mortgage overpayment : 70', 'Council Tax : 207', 'Electricity and Gas : 150.91'] 
assert to_dos[test_key_2] == ['Drink water', 'Take vitamins']

current_tasks = personal_calendar.update_current_tasks(tasks_for_date = date(2024,12,2))

current_task_list = sorted(list(current_tasks.keys()))
assert current_task_list == sorted(['TODO_R_7','TODO_R_8','TODO_S_10','TODO_S_11'])

output_daily_task = sorted(personal_calendar.create_output_daily_task())
check_output = sorted(['Drink water', 'Take vitamins', 'vacuum stairs', 'clean bathrooms'])
assert output_daily_task == check_output





