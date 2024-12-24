import pyodbc
from dotenv import load_dotenv
import os

class objects_from_database:
    def __init__(self, instance, username):
        if instance == 'dev':
            load_dotenv('dev.env')
            self.server = 'your_server.database.windows.net'
            self.database = 'your_database'
        else:
            exit()
        
        self.username = username
    
        def fetch_data_from_sql_server(self, query):
            server = os.getenv('SERVER')
            database = os.getenv('DATABASE')
            username = os.getenv('USER')
            password = os.getenv('PASSWORD')
            
            conn_str = (
                f"DRIVER={{ODBC Driver 17 for SQL Server}};"
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

    def get_user_user_id(self):

        username = self.username

        query = f"""
                    SELECT 
                        id
                    FROM 
                        catalog_users.users 
                    WHERE 
                        username = '{username}'
                """
        
        data = self.fetch_data_from_sql_server(query)

        user_id = data[0]['id']

        self.user_id = user_id
        
        return user_id


x = objects_from_database('dev', 'your_username')
print(x.username)


server = 'your_server.database.windows.net'
database = 'your_database'
username = 'your_username'
password = 'your_password'
query = 'SELECT * FROM your_table'

# data = fetch_data_from_sql_server(server, database, username, password, query)
print(os.getenv('SERVER'))
print(os.getenv('DATABASE'))