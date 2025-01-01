from datetime import date

TEST_events = {
    "PAY_R_1": {
        "name" : "Mortgage",    
        "type" : "payments",
        "dayofmonth": 1,
        "amount": 1000,
        "repeat_type" : "monthly",
        "repeat_period" : 1,
        "account": "Nationwide",
        "weekdays_only" : True
        },
    "PAY_R_2": {
        "name" : "Mortgage overpayment",
        "type" : "payments",
        "dayofweek" : 1,
        "amount": 70,
        "repeat_type" : "weekly",
        "repeat_period" : 1,
        "account": "Nationwide"
        },
    "PAY_R_3": {
        "name" : "Council Tax",
        "type" : "payments",
        "dayofmonth" : 1,
        "amount": 207,
        "repeat_type" : "monthly",
        "account": "Lloyds",
        "weekdays_only" : True
        },
    "PAY_R_4": {
        "name" : "Electricity and Gas",
        "type" : "payments",
        "dayofmonth" : 2,
        "amount": 150.91,
        "repeat_type" : "monthly",
        "repeat_period" : 1,
        "account": "Nationwide",
        "weekdays_only" : True
        },
    "PAY_R_5": {
        "name" : "Water",
        "type" : "payments",
        "dayofmonth" : 6,
        "amount": 150,
        "repeat_type" : "monthly",
        "repeat_period" : 6,
        "account": "Nationwide",
        "weekdays_only" : True,
        "last_triggered" : date(2024, 6, 6),
        "first_occurance" : date(2024, 12, 6)
        },
    "PAY_R_6": {
        "name" : "Broadband",
        "type" : "payments",
        "dayofmonth" : 11,
        "amount": 50,
        "repeat_type" : "monthly",
        "repeat_period" : 1,
        "account": "Lloyds",
        "weekdays_only" : True
        },
    "TODO_R_7" : {
        "name" : "Drink water",
        "type"  : "reminders",
        "timeofday" : "12:00",
        "repeat_type" : "daily",
        "repeat_period" : 1,
        "weekdays_only" : False,
        "max_concurrent_events" : 1
        },
    "TODO_R_8" : {
        "name" : "Take vitamins",
        "type"  : "reminders",
        "timeofday" : "8:00",
        "repeat_type" : "daily",
        "repeat_period" : 1,
        "weekdays_only" : True,
        "max_concurrent_events" : 1
        },
    "TODO_R_9" : {
        "name" : "Complete timesheets",
        "type"  : "reminders",
        "dayofweek" : 4,
        "repeat_type" : "weekly",
        "repeat_period" : 1,
        "max_concurrent_events" : 0
        },
    "TODO_S_10" : {
        "name"  : "clean bathrooms",
        "type"  : "reminders",
        "repeat_type" : "one-off",
    },
    "TODO_S_11" : {
        "name"  : "vacuum stairs",
        "type"  : "reminders",
        "repeat_type" : "one-off",
    }    
    
    }

TEST_date = date(2024, 12, 1)

TEST_outstanding_actions = {
    "TODO_S_10" : {        
        "created" : date(2024, 11, 28),
        "due" : date(2024, 12, 1),
        "status": "outstanding"
        },
    "TODO_S_11" : {
        "created" : date(2024, 11, 30),
        "due": date(2024, 12, 2),
        "status" : "outstanding"
        },
    }