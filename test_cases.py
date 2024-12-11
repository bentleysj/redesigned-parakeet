from datetime import date

TEST_events = {
    "mortgage": {
        "type" : "payments",
        "dayofmonth": 1,
        "amount": 1000,
        "repeate_type" : "monthly",
        "account": "Nationwide",
        "weekdays_only" : True
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
        "account": "Nationwide",
        "weekdays_only" : True
        },
    "Water": {
        "type" : "payments",
        "dayofmonth" : 1,
        "amount": 150,
        "repeate_type" : "six-monthly",
        "account": "Nationwide",
        "weekdays_only" : True
        },
    "Broadband": {
        "type" : "payments",
        "dayofmonth" : 11,
        "amount": 50,
        "repeate_type" : "monthly",
        "account": "Lloyds",
        "weekdays_only" : True
        },
    "Drink water" : {
        "type"  : "reminders",
        "timeofday" : "12:00",
        "repeate_type" : "daily",
        "weekdays_only" : False
        },
    "Take vitamins" : {
        "type"  : "reminders",
        "timeofday" : "8:00",
        "repeate_type" : "daily",
        "weekdays_only" : True
        },
    "Complete timesheets" : {
        "type"  : "reminders",
        "dayofweek" : 4,
        "repeate_type" : "weekly",
        }
    
    }


TEST_date = date(2024, 12, 1)