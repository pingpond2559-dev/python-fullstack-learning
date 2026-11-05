from database import get_db_connection


def get_all_employees():
    mydb = get_db_connection()
    mycursor = None

    try:
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM employees")
        results = mycursor.fetchall()

        return [
            {"id": row[0], "name": row[1], "age": row[2]}
            for row in results
        ]

    finally:
        if mycursor is not None:
            mycursor.close()
        mydb.close()

def get_employee_by_id(employee_id: int):
    mydb = get_db_connection()
    mycursor = mydb.cursor()

    mycursor.execute(
        "SELECT * FROM employees WHERE id = %s",
        (employee_id,)
    )
    result = mycursor.fetchone()

    mycursor.close()
    mydb.close()

    if result is None:
        return None

    return {
        "id": result[0],
        "name": result[1],
        "age": result[2]
    }

def create_employee(name: str, age: int):
    mydb = get_db_connection()
    mycursor = mydb.cursor()

    sql = "INSERT INTO employees (name, age) VALUES (%s, %s)"
    values = (name, age)

    mycursor.execute(sql, values)
    mydb.commit()

    new_id = mycursor.lastrowid

    mycursor.close()
    mydb.close()

    return {
        "id": new_id,
        "name": name,
        "age": age
    }

def delete_employee_by_id(employee_id: int):
    mydb = get_db_connection()
    mycursor = mydb.cursor()

    sql = "DELETE FROM employees WHERE id = %s"
    mycursor.execute(sql, (employee_id,))
    mydb.commit()

    deleted_count = mycursor.rowcount

    mycursor.close()
    mydb.close()

    return deleted_count

def update_employee_by_id(employee_id: int, name: str, age: int):
    mydb = get_db_connection()
    mycursor = mydb.cursor()

    sql = "UPDATE employees SET name = %s, age = %s WHERE id = %s"
    values = (name, age, employee_id)

    mycursor.execute(sql, values)
    mydb.commit()

    updated_count = mycursor.rowcount

    mycursor.close()
    mydb.close()

    return updated_count

def get_employees_over_25():
    mydb = get_db_connection()
    mycursor = mydb.cursor()

    mycursor.execute(
        "SELECT * FROM employees WHERE age > %s",
        (25,)
    )

    results = mycursor.fetchall()

    mycursor.close()
    mydb.close()

    return [
        {"id": row[0], "name": row[1], "age": row[2]}
        for row in results
    ]