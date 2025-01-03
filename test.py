import personal_calendars
import test_cases
from datetime import date

# tests using test cases py dictionary 

calendar_days_to_build = 14
start_date = date(2024, 12, 1)

personal_calendar = personal_calendars.calendars(test_cases.TEST_events, test_cases.TEST_outstanding_actions,  start_date)

calendars = personal_calendar.create_calendars(calendar_days_to_build=calendar_days_to_build)
to_dos, outgoings, total_outgoings = personal_calendar.create_output_calendar()

test_key = start_date.strftime("%a %d %m")
test_key_2 = date(2024,12,2).strftime("%a %d %m")
test_key_3 = date(2024,12,6).strftime("%a %d %m") # test of monthly payment with repeat period of 6 months

assert len(total_outgoings) == calendar_days_to_build
assert len(to_dos) == calendar_days_to_build
assert len(outgoings) == calendar_days_to_build

assert to_dos[test_key] == ["Drink water"]
assert outgoings[test_key] == ["None Scheduled."]
assert total_outgoings[test_key] == 0

assert total_outgoings[test_key_2] == 1277 + 150.91
assert outgoings[test_key_2] == ['Mortgage : 1000', 'Mortgage overpayment : 70', 'Council Tax : 207', 'Electricity and Gas : 150.91'] 
assert outgoings[test_key_3] == ['Water : 150'] 
assert to_dos[test_key_2] == ['Drink water', 'Take vitamins']

current_tasks = personal_calendar.update_current_tasks(tasks_for_date = date(2024,12,2))

current_task_list = sorted(list(current_tasks.keys()))
assert current_task_list == sorted(['TODO_R_7','TODO_R_8','TODO_S_10','TODO_S_11'])

output_daily_task = sorted(personal_calendar.create_output_daily_task())
check_output = sorted(['Drink water', 'Take vitamins', 'vacuum stairs', 'clean bathrooms'])
assert output_daily_task == check_output

import user_catalog

# set for future tests
user_catalog_objects = user_catalog.user_catalog('dev', 'TESTER')
user_catalog_objects.set_user_user_id()

assert user_catalog_objects.user_id == 2

user_catalog_objects.delete_test_data(2)

for event in test_cases.TEST_events:
    user_catalog_objects.add_to_catalog(test_cases.TEST_events[event])

reminders = user_catalog_objects.fetch_catalog('reminders')
payments = user_catalog_objects.fetch_catalog('payments')

assert len(reminders) == 5
assert len(payments) == 6

print("yeah, ok")

