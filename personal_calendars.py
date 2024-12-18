from datetime import date, timedelta
from calendar import monthrange

import test_cases
class calendars:

    def __init__(self, events, start_date = date.today()):

        self.year = start_date.year
        self.month = start_date.month
        self.daysinmonth = monthrange(start_date.year, start_date.month)[1]
        # self.calendar_days_to_calc = calendar_days_to_calc

        self.scheduled_events = events
    
    def get_action_date(self, scheduled_date):
                             
        dow = scheduled_date.isoweekday()
    
        if scheduled_date.isoweekday() in (6,7):
                
                offset = ((7 - scheduled_date.isoweekday()) + 1)
                
                action_date = scheduled_date + timedelta(days = offset)

        else:

            action_date = scheduled_date

        return action_date        

    def add_to_outgoings(self, date, event): 

        amount = self.scheduled_events[event]["amount"]

        if date not in self.total_outgoings_calendar.keys():

            self.total_outgoings_calendar[date] = amount

        else:

            self.total_outgoings_calendar[date] = self.total_outgoings_calendar[date] + amount

        return 0
    
    def add_to_to_do(self, date, event):

        event_type = self.scheduled_events[event]['type']

        if event_type == "payments":

            amount = self.scheduled_events[event]["amount"]

            if date not in self.outgoings_calendar.keys():

                self.outgoings_calendar[date] = [f"{event}: {amount}"]

            else:

                self.outgoings_calendar[date].append(f"{event}: {amount}")
        
        elif event_type == "reminders":

            if date not in self.to_do_calendar.keys():

                self.to_do_calendar[date] = [event]

            else:

                self.to_do_calendar[date].append(event)

        return 0
    
    def add_to_calendar(self, event, date):
    
        event_type = self.scheduled_events[event]['type']

        if event_type == "payments":
              
            self.add_to_outgoings(date, event)
            self.add_to_to_do(date, event)
        
        elif event_type == "reminders":

            calendar = self.add_to_to_do(date, event)
           
        return 0

    def create_calendars(self, start_date = date.today(), calendar_days_to_build = 30):

        date_range = [start_date + timedelta(days = i) for i in range(calendar_days_to_build)]   

        self.total_outgoings_calendar = {} 
        self.outgoings_calendar = {} 
        self.to_do_calendar = {} 

        outgoings = self.scheduled_events
        # TODO: six-monthly, yearly, etc. 
        # TODO: too much nesting - move more into functions

        for event in outgoings:

            if outgoings[event]["repeate_type"] == "monthly":

                for month_to_build in range(date_range[0].month, date_range[-1].month + 1):

                    scheduled_date = date(self.year, month_to_build, outgoings[event]["dayofmonth"])

                    if outgoings[event]["weekdays_only"] == True:

                        action_date = self.get_action_date(scheduled_date)
                        
                    else:
                        
                        action_date = scheduled_date

                    if action_date in date_range:

                            self.add_to_calendar(event, action_date)

            elif outgoings[event]["repeate_type"]  == "weekly":

                    for day in date_range:

                        if day.isoweekday() == outgoings[event]["dayofweek"]:

                            self.add_to_calendar(event, day)

            elif outgoings[event]["repeate_type"] == "daily":
                        
                for day in date_range:

                    if outgoings[event]["weekdays_only"] == False or day.isoweekday() not in (6,7):

                        self.add_to_calendar(event, day)

        return self.total_outgoings_calendar, self.to_do_calendar, self.outgoings_calendar
    
    # TODO: daily plan

    def get_daily_outgoing(self, date):

        daily_outgoing = 0


