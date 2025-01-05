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
        
        self.username = os.getenv('SQL_SERVER_USERNAME')
        self.password = os.getenv('SQL_SERVER_PASSWORD')
        self.server   = os.getenv('SQL_SERVER')
        self.database = os.getenv('SQL_SERVER_DATABASE')        

    def fetch_data_from_sql_server(self, query, query_type = 'select'):
                
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

        
        
        if query_type == 'insert':    
            cursor.execute(query)
            cursor.execute("SELECT SCOPE_IDENTITY()")
            new_id = cursor.fetchone()[0]
            conn.commit()  
            cursor.close()

            conn.close()

            return new_id
        
        elif query_type == 'select':
            cursor.execute(query)
            rows = cursor.fetchall()
            columns = [column[0] for column in cursor.description]
            result = [dict(zip(columns, row)) for row in rows]
            cursor.close()
            conn.close()

            return result
        
        else:
            cursor.execute(query)
            conn.commit()  
            cursor.close()
            conn.close()

            return 0

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
        
        new_event_id = self.fetch_data_from_sql_server(query, 'insert')

        return new_event_id
    
    def delete_test_data(self, test_user_id):

        query = f"""
                    delete from TASK_CATALOG.TASK_INSTANCES
                    where USER_ID = {test_user_id}
                """
        
        self.fetch_data_from_sql_server(query, 'delete')

        query = f"""
                    delete from TASK_CATALOG.TASKS
                    where USER_ID = {test_user_id}
                """
        
        self.fetch_data_from_sql_server(query, 'delete')

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
    
    def get_event_details(self, event_id):

        user_id = self.user_id

        query = f"""
                    SELECT
                        *
                    FROM 
                        TASK_CATALOG.TASKS
                    WHERE 
                        USER_ID = {user_id}
                        AND EVENT_ID = {event_id}
                """
        
        data = self.fetch_data_from_sql_server(query, 'select')

        return data
    
    def create_event_instance(self, event_id, trigger_at = datetime.now()):

        event_details = self.get_event_details(event_id)[0]

        user_id = self.user_id
        event_id = event_details.get('EVENT_ID')

        if trigger_at <= datetime.now():
            status = 'ACTIVE'
        elif trigger_at > datetime.now():
            status = 'PENDING'
        
        created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        finished_at = 'NULL'
        last_updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        active = 1
        
        query = f"""
                    insert into TASK_CATALOG.TASK_INSTANCES
                    (
                        USER_ID
                        ,EVENT_ID
                        ,STATUS
                        ,CREATED
                        ,FINISHED_AT
                        ,LAST_UPDATED_AT
                        ,ACTIVE
                    )
                    values
                    (
                        {user_id}
                        ,{event_id}
                        ,'{status}'
                        ,'{created}'
                        ,{finished_at}
                        ,'{last_updated}'
                        ,{active}
                    );
                """
        
        event_instance_id = self.fetch_data_from_sql_server(query, 'insert')

        return event_instance_id

    def create_one_off_event(self, event, trigger_at = datetime.now()):
        
        event_id = self.add_to_catalog(event)

        event_instance_id = self.create_event_instance(event_id, trigger_at)

        return f'Event {event_id} added to catalog, instance: {event_instance_id} created'













    


