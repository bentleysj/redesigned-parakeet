from datetime import date, timedelta
from calendar import monthrange

import test_cases
class monthly_outgoings:

    def __init__(self, date, events, start_date = date.today()):

        self.year = date.year
        self.month = date.month
        self.daysinmonth = monthrange(date.year, date.month)[1]
        # self.calendar_days_to_calc = calendar_days_to_calc

        self.regular_outgoings = events
    
    def get_action_date(self, scheduled_date):
                             
        dow = scheduled_date.isoweekday()
    
        if scheduled_date.isoweekday() in (6,7):
                
                offset = ((7 - scheduled_date.isoweekday()) + 1)
                
                action_date = scheduled_date + timedelta(days = offset)

        else:

            action_date = scheduled_date

        return action_date        

    # TODO: daily plan

    def add_to_outgoings(self, date, event): 

        amount = self.regular_outgoings[event]["amount"]

        if date not in self.outgoings_calendar.keys():

            self.outgoings_calendar[date] = amount

        else:

            self.outgoings_calendar[date] = self.outgoings_calendar[date] + amount

        return 0
    
    def add_to_to_do(self, date, event):
                
        if date not in self.to_do_calendar.keys():

            self.to_do_calendar[date] = [event]

        else:

            self.to_do_calendar[date].append(event)

        return 0
    
    def add_to_calendar(self, event, date):
    
        event_type = self.regular_outgoings[event]['type']

        if event_type == "payments":
              
            calendar = self.add_to_outgoings(date, event)
        
        elif event_type == "reminders":

            calendar = self.add_to_to_do(date, event)
           
        return 0

    def create_outgoings_calendar(self, start_date = date.today(), calendar_days_to_build = 30):
        # forward looking - 
        # TODO: build a week and month ahead.true

        # days_ahead_to_build = self.calendar_days_to_calc

        date_range = [start_date + timedelta(days = i) for i in range(calendar_days_to_build)]   

        self.outgoings_calendar = {} 
        # {date for date in date.range(start_date, start_date + timedelta(days = calendar_days_to_build))}
        # print(date_range.keys())
        # outgoings_calendar = {}
        self.to_do_calendar = {} 
        # {date for date in range(start_date, start_date + timedelta(days = calendar_days_to_build))}

        outgoings = self.regular_outgoings
        # TODO: make actions for weekly and six-monthly
        # TODO: refactor logic - repeate type > type
        # TODO: refactor logic - work with dates
        # TODO: refactor logic - start dates 

        for event in outgoings:

            if outgoings[event]["repeate_type"] == "monthly":

                if outgoings[event]["type"] == "payments":

                    scheduled_date = date(self.year, self.month, outgoings[event]["dayofmonth"])
                    action_date = self.get_action_date(scheduled_date)

                    self.add_to_calendar(event, action_date)

            elif outgoings[event]["repeate_type"]  == "weekly":

                    for day in date_range:

                        if day.isoweekday() == outgoings[event]["dayofweek"]:

                            self.add_to_calendar(event, day)

            elif outgoings[event]["repeate_type"] == "daily":
                        
                for day in date_range:

                    self.add_to_calendar(event, day)

        return self.outgoings_calendar, self.to_do_calendar     

    def get_daily_outgoing(self, date):

        daily_outgoing = 0


monthly_expenses = monthly_outgoings(test_cases.TEST_date, test_cases.TEST_events)

calendars = monthly_expenses.create_outgoings_calendar(calendar_days_to_build=7)

print(monthly_expenses.outgoings_calendar)
print(monthly_expenses.to_do_calendar)