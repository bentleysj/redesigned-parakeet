from datetime import date
from calendar import monthrange


TEST_events = {
    "mortgage": {
        "dayofmonth": 1,
        "amount": 1000,
        "repeate_type" : "monthly",
        "account": "Nationwide"
        },
    "morgate_overpayment": {
        "dayofweek" : 1,
        "amount": 70,
        "repeate_type" : "weekly",
        "account": "Nationwide"
        },
    "Council Tax": {
        "dayofmonth" : 1,
        "amount": 207,
        "repeate_type" : "monthly",
        "account": "Lloyds"
        },
    "Electricity and Gas": {
        "dayofmonth" : 2,
        "amount": 150.91,
        "repeate_type" : "monthly",
        "account": "Nationwide"
        }}

TEST_date = date(2024, 11, 1)

class monthly_outgoings:

    def __init__(self, date, events):

        self.year = date.year
        self.month = date.month
        self.daysinmonth = monthrange(date.year, date.month)[1]

        self.regular_outgoings = events

    def create_outgoings_calendar(self):

        outgoings_calendar = {}

        outgoings = self.regular_outgoings

        for event in outgoings:

            if outgoings[event]["repeate_type"] == "monthly":

                if outgoings[event]["dayofmonth"] not in outgoings_calendar.keys():

                    outgoings_calendar[outgoings[event]["dayofmonth"]] = outgoings[event]["amount"]

                else:

                    outgoings_calendar[outgoings[event]["dayofmonth"]] = outgoings_calendar[outgoings[event]["dayofmonth"]] + outgoings[event]["amount"]

            elif outgoings[event]["repeate_type"]  == "weekly":

                for day in range(1, self.daysinmonth + 1):
                    print(date(self.year, self.month, day), date(self.year, self.month, day).isoweekday())
                    if date(self.year, self.month, day).isoweekday() == outgoings[event]["dayofweek"]:

                        if day not in outgoings_calendar.keys():

                            outgoings_calendar[day] = outgoings[event]["amount"]

                        else:

                            outgoings_calendar[day] = outgoings_calendar[day] + outgoings[event]["amount"]

        return outgoings_calendar      



    def get_daily_outgoing(self, date):

        daily_outgoing = 0


monthly_expenses = monthly_outgoings(TEST_date, TEST_events)

print(monthly_expenses.create_outgoings_calendar())
        
