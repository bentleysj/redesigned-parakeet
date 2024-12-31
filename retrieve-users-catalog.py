import pyodbc
from dotenv import load_dotenv
import os

class objects_from_database:
    def __init__(self, instance, app_username):
        if instance == 'dev':
            load_dotenv('dev.env')
        else:
            exit()
        
        self.username = os.getenv('USERNAME')
        self.password = os.getenv('PASSWORD')
        self.server   = os.getenv('SERVER')
        self.database = os.getenv('DATABASE')        

    def fetch_data_from_sql_server(self, query):
                
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
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
        cursor.close()
        conn.close()

        return result

def set_user_user_id(self):

    app_user = self.app_user

    query = f"""
                SELECT 
                    id
                FROM 
                    catalog_users.users 
                WHERE 
                    username = '{app_user}'
            """
    
    data = self.fetch_data_from_sql_server(query)

    user_id = data[0]['id']

    self.user_id = user_id
    
    return 0