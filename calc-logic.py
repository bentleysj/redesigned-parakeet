from datetime import date
from calendar import monthrange


TEST_events = {
    "mortgage": {
        "type" : "payments",
        "dayofmonth": 1,
        "amount": 1000,
        "repeate_type" : "monthly",
        "account": "Nationwide"
        },
    "morgate_overpayment": {
        "type" : "payments",
        "dayofweek" : 1,
        "amount": 70,
        "repeate_type" : "weekly",
        "account": "Nationwide"
        },
    "Council Tax": {
        "type" : "payments",
        "dayofmonth" : 1,
        "amount": 207,
        "repeate_type" : "monthly",
        "account": "Lloyds"
        },
    "Electricity and Gas": {
        "type" : "payments",
        "dayofmonth" : 2,
        "amount": 150.91,
        "repeate_type" : "monthly",
        "account": "Nationwide"
        },
    "Water": {
        "type" : "payments",
        "dayofmonth" : 1,
        "amount": 150,
        "repeate_type" : "six-monthly",
        "account": "Nationwide"
        },
    "Broadband": {
        "type" : "payments",
        "dayofmonth" : 11,
        "amount": 50,
        "repeate_type" : "monthly",
        "account": "Lloyds"
        },
    "Drink water" : {
        "type"  : "reminders",\
        "timeofday" : "12:00",
        "repeate_type" : "daily",
        },
    "Take vitamins" : {
        "type"  : "reminders",\
        "timeofday" : "8:00",
        "repeate_type" : "daily",
        },
    "Complete timesheets" : {
        "type"  : "reminders",\
        "dayofweek" : 4,
        "repeate_type" : "weekly",
        }
    
    }

TEST_date = date(2024, 12, 1)

class monthly_outgoings:

    def __init__(self, date, events):

        self.year = date.year
        self.month = date.month
        self.daysinmonth = monthrange(date.year, date.month)[1]

        self.regular_outgoings = events
    
    def get_action_date(self, dayofmonth):

        scheduled_date = date(self.year, self.month, dayofmonth)
        dow = scheduled_date.isoweekday()
        if scheduled_date.isoweekday() in (6,7):
                
                offset = ((7 - scheduled_date.isoweekday()) + 1)
                
                action_date = dayofmonth + offset

        else:

            action_date = dayofmonth

        return action_date        

    # TODO: daily plan

    def create_outgoings_calendar(self):
        # forward looking - 
        # TODO: build a week and month ahead.
        
        outgoings_calendar = {}
        to_do_calendar = {}

        outgoings = self.regular_outgoings
        # TODO: make actions for weekly and six-monthly
        # TODO: refactor logic - repeate type > type
        # TODO: refactor logic - work with dates
        # TODO: refactor logic - start dates 
        for event in outgoings:

            if outgoings[event]["type"] == "payments":

                if outgoings[event]["repeate_type"] == "monthly":
                    
                    action_date = self.get_action_date(outgoings[event]["dayofmonth"])

                    if action_date not in outgoings_calendar.keys():

                        outgoings_calendar[action_date] = outgoings[event]["amount"]

                    else:

                        outgoings_calendar[action_date] = outgoings_calendar[action_date] + outgoings[event]["amount"]

                elif outgoings[event]["repeate_type"]  == "weekly":

                    for day in range(1, self.daysinmonth + 1):

                        if date(self.year, self.month, day).isoweekday() == outgoings[event]["dayofweek"]:

                            if day not in outgoings_calendar.keys():

                                outgoings_calendar[day] = outgoings[event]["amount"]

                            else:

                                outgoings_calendar[day] = outgoings_calendar[day] + outgoings[event]["amount"]
            else:   
                if outgoings[event]["type"] == "reminders":

                    if outgoings[event]["repeate_type"] == "daily":
                        
                        for day in range(1, self.daysinmonth + 1):
                                
                                if day not in to_do_calendar.keys():
    
                                    to_do_calendar[day] = [event]
    
                                else:
    
                                    to_do_calendar[day] = to_do_calendar[day].append(event)




        return outgoings_calendar, to_do_calendar     



    def get_daily_outgoing(self, date):

        daily_outgoing = 0


monthly_expenses = monthly_outgoings(TEST_date, TEST_events)

calendars = monthly_expenses.create_outgoings_calendar()
print(calendars[0])
print(calendars[1])
        
