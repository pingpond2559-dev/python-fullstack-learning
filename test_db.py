
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Over2489+za",
    database="company_db"
)

print("Connected to MySQL successfully!")

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM employees")

results = mycursor.fetchall()

for employee in results:
    print(employee)

mycursor.close()
mydb.close()




