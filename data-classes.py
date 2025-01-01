import dataclasses
from datetime import date, time
from decimal import Decimal

@dataclasses.dataclass(frozen=True, order=True)
class todo_events:
    event_id: int
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





    def __str__(self):
        return f'{self.event_id} {self.event_name} {self.event_date} {self.event_time} {self.event_location}'