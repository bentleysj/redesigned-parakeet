import pyodbc

def fetch_data_from_sql_server(server, database, username, password, query):
    # Define the connection string
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password}"
    )
    
    # Establish the connection
    conn = pyodbc.connect(conn_str)
    
    # Create a cursor object
    cursor = conn.cursor()
    
    # Execute the query
    cursor.execute(query)
    
    # Fetch all rows from the executed query
    rows = cursor.fetchall()
    
    # Get column names from the cursor description
    columns = [column[0] for column in cursor.description]
    
    # Convert rows to a list of dictionaries
    result = [dict(zip(columns, row)) for row in rows]
    
    # Close the cursor and connection
    cursor.close()
    conn.close()
    
    return result


server = 'your_server.database.windows.net'
database = 'your_database'
username = 'your_username'
password = 'your_password'
query = 'SELECT * FROM your_table'

data = fetch_data_from_sql_server(server, database, username, password, query)
print(data)