import sqlite3

# Create a connection to a new SQLite database or connect to an existing one
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()



# Define the SQL statement to create the table
create_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        email TEXT
    )
'''

# Execute the SQL statement to create the table
cursor.execute(create_table_query)

# Define the data to be inserted
name = 'John Doe'
age = 30
email = 'johndoe@example.com'

# Execute an SQL INSERT statement
cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", (name, age, email))

# Commit the changes to the database
conn.commit()


users = cursor.execute("SELECT * FROM users")

parsed_users = []
for user in users:
    user_id, name, age, email = user
    parsed_users.append({
        'id': user_id,
        'name': name,
        'age': age,
        'email': email
    })

# Print the parsed users list
for user in parsed_users:
    print(f"ID: {user['id']}")
    print(f"Name: {user['name']}")
    print(f"Age: {user['age']}")
    print(f"Email: {user['email']}")
    print()

conn.close()