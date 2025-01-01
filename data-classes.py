import dataclasses
from datetime import date, time, datetime
from decimal import Decimal

@dataclasses.dataclass(frozen=True, order=True)
class todo_events:
    event_id: int

    user_id: int

    event_name: str
    event_type: str # payments, todos, lists?

    repeat_type: str # daily, weekly, monthly+, 
    repeat_period: int # 1 = every, etc. 

    time_of_day: time 
    day_of_month: int 
    day_of_week: int
    
    weekdays_only: bool
    max_concurrency = int
    event_persists = bool

    # payments
    account: str
    ammount: Decimal

    # meta
    created_date: datetime
    most_recent_trigger: datetime
    first_scheduled_instance: date

    def __str__(self):
        return f'{self.event_id}: {self.event_name}'

    def repeat_detail(self):    
        
        if self.repeat_type == 'daily':
            repeating_detail =  f'{self.repeat_period} days '
        elif self.repeat_type == 'weekly':
            repeating_detail =  f'{self.repeat_period} weeks'
        elif self.repeat_type == 'monthly':
            repeating_detail = f'{self.repeat_period} months'
        else:
            return 'one-off'
        
        if self.weekdays_only:
            repeating_detail += ' weekdays only'
        
        if self.max_concurrency == 1:
            repeating_detail += ' One Instance Only'
        elif self.max_concurrency > 1:
            repeating_detail += f' Max {self.max_concurrency} instances'
        
        return repeating_detail