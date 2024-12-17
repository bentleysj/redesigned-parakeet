import personal_calendars
import test_cases

calendar_days_to_build = 14
start_date = test_cases.TEST_date

personal_calendar = personal_calendars.calendars(test_cases.TEST_events, start_date)
total_outgoings, to_dos, outgoings = personal_calendar.create_calendars(start_date, calendar_days_to_build=calendar_days_to_build)

