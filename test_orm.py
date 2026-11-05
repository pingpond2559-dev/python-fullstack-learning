
from orm_database import SessionLocal
from models import EmployeeModel

db = SessionLocal()

try:
    employee = (
        db.query(EmployeeModel)
        .filter(EmployeeModel.id == 165010)
        .first()
    )

    if employee is None:
        print("Verified: Employee not found")
    else:
        print("Employee still exists")

finally:
    db.close()
