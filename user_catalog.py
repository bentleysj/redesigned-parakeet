import pyodbc
from dotenv import load_dotenv
import os
from datetime import datetime

class user_catalog:
    def __init__(self, instance, app_username):

        self.app_username = app_username

        if instance == 'dev':
            load_dotenv('dev.env', override=True)
        else:
            exit()
        
        self.username = os.getenv('USERNAME')
        self.password = os.getenv('PASSWORD')
        self.server   = os.getenv('SERVER')
        self.database = os.getenv('DATABASE')        

    def fetch_data_from_sql_server(self, query, update = False):
                
        username = self.username
        password = self.password
        server   = self.server
        database = self.database      
        
        conn_str = (
            f"DRIVER={{ODBC Driver 18 for SQL Server}};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"UID={username};"
            f"PWD={password}"
        )

        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute(query)

        if update == True:
            conn.commit()
            cursor.close()
            conn.close()
            return 0
        
        else:
        
            rows = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            result = [dict(zip(columns, row)) for row in rows]
            cursor.close()
            conn.close()

            return result

    def set_user_user_id(self):

        app_username = self.app_username

        query = f"""
                    SELECT 
                        id
                    FROM 
                        TASK_USERS.USERS
                    WHERE 
                        username = '{app_username}'
                """
        
        data = self.fetch_data_from_sql_server(query)

        user_id = data[0]['id']

        self.user_id = user_id
        
        return 0
    
    def create_user(self, email, password):

        app_username = self.app_username

        query = f"""
                    insert into 
                        TASK_USERS.USERS
                        (
                            USERNAME,
                            PASSWORD,
                            EMAIL,
                            CREATED_AT,
                            LAST_UPDATED_AT
                        )
                        values
                        (
                            '{app_username}',
                            '{email}',
                            '{password}',
                            CURRENT_TIMESTAMP,
                            CURRENT_TIMESTAMP
                        );
                """
        
        self.fetch_data_from_sql_server(query)
        self.set_user_user_id()

        return 0
    
    def add_to_catalog(self, event):

        user_id = self.user_id

        event_name = event.get('name')
        event_type = event.get('type')        

        task_details = event.get('task_details','NULL')
        created_at = event.get('created_at',datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        most_recent_trigger = event.get('most_recent_trigger',datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        first_occurance = event.get('first_occurance',datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        time_of_day = event.get('timeofday','00:00:00')
        day_of_month = event.get('dayofmonth',0)
        day_of_week = event.get('dayofweek',0)
        
        repeat_type = event.get('repeat_type')
        repeat_period = event.get('repeat_period','NULL')

        weekdays_only = int(event.get('weekdays_only',False))
        max_concurrent = event.get('max_concurrent_events',0)
        event_persists = int(event.get('event_persists',True))

        amount = event.get('amount',0)
        account = event.get('account','NOT SPECIFIED')

        classify_id = str(user_id) + '-' + event_type[0] + '_' + repeat_type[0]

        query = f"""
                    insert into TASK_CATALOG.TASKS
                    (
                    
                    USER_ID
                    ,CLASSIFYING_ID
                    ,EVENT_NAME                    
                    ,EVENT_TYPE
                    ,TASK_DETAILS
                    ,CREATED_AT
                    ,MOST_RECENT_TRIGGER
                    ,FIRST_OCCURANCE
                    ,TIME_OF_DAY
                    ,DAY_OF_MONTH
                    ,DAY_OF_WEEK
                    ,REPEAT_TYPE
                    ,REPEAT_PERIOD
                    ,WEEKDAYS_ONLY
                    ,MAX_CONCURRENT
                    ,EVENT_PERSISTS
                    ,AMOUNT
                    ,ACCOUNT
                    )
                    values
                    (
                    {user_id}
                    ,'{classify_id}'
                    ,'{event_name}'
                    ,'{event_type}'
                    ,'{task_details}'
                    ,'{created_at}'
                    ,'{most_recent_trigger}'
                    ,'{first_occurance}'
                    ,'{time_of_day}'
                    ,{day_of_month}
                    ,{day_of_week}
                    ,'{repeat_type}'
                    ,{repeat_period}
                    ,{weekdays_only}
                    ,{max_concurrent}
                    ,{event_persists}
                    ,{amount}
                    ,'{account}'
                    );  
                """
        
        self.fetch_data_from_sql_server(query, update = True)

        return 0
    
    def delete_test_data(self, test_user_id):

        query = f"""
                    delete from TASK_CATALOG.TASKS
                    where USER_ID = {test_user_id}
                """
        
        self.fetch_data_from_sql_server(query, update = True)

        return 0

    def fetch_catalog(self, event_type):

        user_id = self.user_id

        query = f"""
                    SELECT 
                        *
                    FROM 
                        TASK_CATALOG.TASKS
                    WHERE 
                        USER_ID = {user_id}
                        AND EVENT_TYPE = '{event_type}'
                """
        
        data = self.fetch_data_from_sql_server(query)

        return data











    


