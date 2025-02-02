from datetime import date, timedelta
from calendar import monthrange

import test_cases
class calendars:

    def __init__(self, events, outstanding_tasks = {}, start_date = date.today()):

        self.start_date = start_date

        self.current_to_do_list = outstanding_tasks

        self.year = start_date.year
        self.month = start_date.month
        self.daysinmonth = monthrange(start_date.year, start_date.month)[1]

        self.scheduled_events = events
    
    def get_action_date(self, scheduled_date):                             
    
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
            event_name = self.scheduled_events[event]["name"]

            if date not in self.outgoings_calendar.keys():                
                self.outgoings_calendar[date] = [event]

            else:
                self.outgoings_calendar[date].append(event)
        
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
    
    def get_event_name(self, event):

        if self.scheduled_events[event]["type"] == "payments":
            event_name = self.scheduled_events[event]["name"] + " : " + str(self.scheduled_events[event]["amount"])

        elif self.scheduled_events[event]["type"] == "reminders":
            event_name = self.scheduled_events[event]["name"]

        return event_name

    def get_event_names_for_day(self, calendar, date):

        if date in calendar.keys():
            events = calendar[date]
            event_names = [self.get_event_name(event) for event in events]

        else:
            event_names = ['None Scheduled.']

        return event_names
    
    def get_next_occurance(self, event):

        next_occurance = date(1970,1,1)

        if self.scheduled_events[event]["first_occurance"] > self.start_date:

            next_occurance = self.scheduled_events[event]["first_occurance"]

        elif self.scheduled_events[event]["repeat_period"] > 1:

            reference_occurance = max(self.scheduled_events[event]["last_triggered"], self.scheduled_events[event]["first_occurance"])

            if self.scheduled_events[event]["repeat_type"] == "monthly":
                next_occurance = reference_occurance + timedelta(months = self.scheduled_events[event]["repeat_period"])
            elif self.scheduled_events[event]["repeat_type"] == "weekly":
                next_occurance = reference_occurance + timedelta(weeks = self.scheduled_events[event]["repeat_period"])
            elif self.scheduled_events[event]["repeat_type"] == "daily":
                next_occurance = reference_occurance + timedelta(days = self.scheduled_events[event]["repeat_period"])
            
        return next_occurance

    def create_calendars(self, calendar_days_to_build = 30):

        start_date = self.start_date
        self.calendar_days_to_build = calendar_days_to_build
        date_range = [start_date + timedelta(days = i) for i in range(calendar_days_to_build)]   

        self.total_outgoings_calendar = {} 
        self.outgoings_calendar = {} 
        self.to_do_calendar = {} 

        outgoings = self.scheduled_events
        # TODO: six-monthly, yearly, etc. 
        # TODO: too much nesting - move more into functions

        for event in outgoings:
            if outgoings[event]["repeat_type"] == "monthly":

                    for month_to_build in range(date_range[0].month, date_range[-1].month + 1):

                        if outgoings[event].get("repeat_period",1) > 1:
                            scheduled_date = self.get_next_occurance(event)
                        else:                        
                            scheduled_date = date(self.year, month_to_build, outgoings[event]["dayofmonth"])

                        if outgoings[event]["weekdays_only"] == True:
                            action_date = self.get_action_date(scheduled_date)                            
                        else:                        
                            action_date = scheduled_date

                        if action_date in date_range:
                            self.add_to_calendar(event, action_date)

            elif outgoings[event]["repeat_type"]  == "weekly":

                    for day in date_range:

                        if day.isoweekday() == outgoings[event]["dayofweek"]:
                            self.add_to_calendar(event, day)

            elif outgoings[event]["repeat_type"] == "daily":
                        
                for day in date_range:

                    if outgoings[event]["weekdays_only"] == False or day.isoweekday() not in (6,7):
                        self.add_to_calendar(event, day)

        return (self.total_outgoings_calendar, self.to_do_calendar, self.outgoings_calendar)

    def create_output_calendar(self):

        total_outgoings = self.total_outgoings_calendar
        to_dos = self.to_do_calendar
        outgoings = self.outgoings_calendar

        start_date = self.start_date
        calendar_days_to_build = self.calendar_days_to_build

        ren_personal_calendar = {}
        ren_outgoing_calendar = {}
        ren_total_outgoing_calendar = {}
        dates = [(start_date + timedelta(days=i)) for i in range(calendar_days_to_build)]

        for date in dates:

            if date in total_outgoings.keys():
                total_outgoing = total_outgoings[date]
            else:
                total_outgoing = 0
                
            todo = self.get_event_names_for_day(to_dos, date)
            outgoing = self.get_event_names_for_day(outgoings, date)

            ren_personal_calendar[date.strftime("%a %d %m")] =  todo
            ren_outgoing_calendar[date.strftime("%a %d %m")] =  outgoing
            ren_total_outgoing_calendar[date.strftime("%a %d %m")] =  total_outgoing

        return ren_personal_calendar, ren_outgoing_calendar, ren_total_outgoing_calendar
                   
    def update_current_tasks(self, tasks_for_date = date.today()):

        current_to_do_list = self.current_to_do_list
        new_to_add = self.to_do_calendar[tasks_for_date]
        
        for to_do in new_to_add:

            if to_do not in current_to_do_list:

                current_to_do_list[to_do] = {"created": date.today(),
                                            "due": date.today(),
                                            "status": "outstanding"}
                
        self.current_to_do_list = current_to_do_list

        return current_to_do_list
    
    def create_output_daily_task(self):

        ouput_task_list = []

        if len(self.current_to_do_list) == 0:
            ouput_task_list = ["None Scheduled."]
    
        for task in self.current_to_do_list:
            
            self.current_to_do_list[task]["name"] = self.scheduled_events[task]["name"]

            task_name = self.get_event_name(task)
            ouput_task_list.append(task_name)

        return ouput_task_list



