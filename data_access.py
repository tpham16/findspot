import sqlite3

# Establish a connection to the database
conn = sqlite3.connect('lost_pets.db')

# Create a cursor object
cursor = conn.cursor()

# Execute a SELECT query
cursor.execute("SELECT * from lost_pets")

# Fetch all rows from the query result
rows = cursor.fetchall()

# Process the retrieved data
for row in rows:
    print(row)  
    
# Close the connection
conn.close()