import psycopg2

# Database connection details
DB_NAME = "menues"  # Replace with your database name
USER = "postgres"          # Replace with your PostgreSQL username
PASSWORD = ""      # Replace with your password
HOST = "localhost"              # Replace with your host (likely localhost)
PORT = "5432"                   # Replace with your port (default: 5432)

try:
    # Establish the connection
    connection = psycopg2.connect(
        dbname=DB_NAME,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )
    print("Connection successful!")
    
    # Create a cursor
    cursor = connection.cursor()
    
    # Example: Execute a query
    query = "SELECT version();"
    cursor.execute(query)
    
    # Fetch the result
    result = cursor.fetchone()
    print(f"PostgreSQL version: {result[0]}")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the connection
    if 'connection' in locals() and connection:
        connection.close()
        print("Connection closed.")
