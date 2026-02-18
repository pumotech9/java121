'''import mysql.connector

# 1. Establish connection (mydb)
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="madhu",
  database="hosur"
)

# 2. Create cursor object (mycursor)
mycursor = mydb.cursor()

# 3. Execute query
mycursor.execute("SELECT * FROM student")

# 4. Fetch results
for row in mycursor.fetchall():
  print(row)

# 5. Close connections
mycursor.close()
mydb.close()
'''
