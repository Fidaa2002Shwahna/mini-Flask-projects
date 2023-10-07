import pymysql

conn = pymysql.connect(
  host='sql12.freesqldatabase.com',
  database='sql12651524',
  user='sql12651524',
  password='DislAzX9fi',
  charset='utf8mb4',
  cursorclass=pymysql.cursors.DictCursor
)
cursor = conn.cursor()

# Create the 'books' table if it doesn't exist
sql_query = """CREATE TABLE IF NOT EXISTS books (
  id integer PRIMARY KEY,
  author text NOT NULL,
  language text NOT NULL,
  title text NOT NULL
)"""
cursor.execute(sql_query)

# Execute a SELECT query to retrieve data from the 'books' table
select_query = "SELECT * FROM books"
cursor.execute(select_query)

# Fetch all the rows from the result set
result = cursor.fetchall()

# Display the values
for row in result:
    print(f"ID: {row['id']}, Author: {row['author']}, Language: {row['language']}, Title: {row['title']}")

# Close the cursor and connection
cursor.close()
conn.close()
