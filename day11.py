mydb = get_db_connection()

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM employees")
results = mycursor.fetchall()