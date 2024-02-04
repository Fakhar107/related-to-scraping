import sqlite3

# Connect to SQLite database (create it if not exists)
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER)''')

# Insert data into the table
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 30))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Bob', 25))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Charlie', 35))

# Commit the changes
conn.commit()

# Retrieve data from the table
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Print the retrieved data
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
