
from fastapi import APIRouter, HTTPException
from schemas import Employee, EmployeeResponse, EmployeeUpdate
from fastapi import Depends
from sqlalchemy.orm import Session
from orm_dependencies import get_db
from models import EmployeeModel


router = APIRouter()


@router.get("/")
def name():
    return {
        "name": "Ping",
        "age": 24,
        "position": "Python Developer"
    }


@router.get("/employees/over-25", response_model=list[EmployeeResponse])
def get_employees_over_25_endpoint(
    db: Session = Depends(get_db)
):
    employees = (
        db.query(EmployeeModel)
        .filter(EmployeeModel.age > 25)
        .all()
    )
    return employees


@router.get(
    "/employees/{employee_id}",
    response_model=EmployeeResponse
)
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    employee = (
        db.query(EmployeeModel)
        .filter(EmployeeModel.id == employee_id)
        .first()
    )

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return employee



@router.get("/employees", response_model=list[EmployeeResponse])
def get_employees(db: Session = Depends(get_db)):
    employees = db.query(EmployeeModel).all()
    return employees


@router.post(
    "/employees",
    response_model=EmployeeResponse,
    status_code=201
)
def create_employee_endpoint(
    employee: Employee,
    db: Session = Depends(get_db)
):
    try:
        new_employee = EmployeeModel(
            name=employee.name,
            age=employee.age
        )

        db.add(new_employee)
        db.commit()
        db.refresh(new_employee)

        return new_employee

    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Failed to create employee"
        )

@router.delete("/employees/{employee_id}")
def delete_employee_endpoint(
    employee_id: int,
    db: Session = Depends(get_db)
):
    employee_db = (
        db.query(EmployeeModel)
        .filter(EmployeeModel.id == employee_id)
        .first()
    )

    if employee_db is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    try:
        db.delete(employee_db)
        db.commit()

        return {
            "message": f"Employee {employee_id} deleted successfully"
        }

    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Failed to delete employee"
        )

@router.put(
    "/employees/{employee_id}",
    response_model=EmployeeResponse
)
def update_employee_endpoint(
    employee_id: int,
    employee: Employee,
    db: Session = Depends(get_db)
):
    employee_db = (
        db.query(EmployeeModel)
        .filter(EmployeeModel.id == employee_id)
        .first()
    )

    if employee_db is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    try:
        employee_db.name = employee.name
        employee_db.age = employee.age

        db.commit()
        db.refresh(employee_db)

        return employee_db

    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Failed to update employee"
        )


@router.patch("/employees/{employee_id}", response_model=EmployeeResponse)
def patch_employee_endpoint(
    employee_id: int,
    employee: EmployeeUpdate,
    db: Session = Depends(get_db)
):
    employee_db = (
        db.query(EmployeeModel)
        .filter(EmployeeModel.id == employee_id)
        .first()
    )

    if employee_db is None:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    try:
        update_data = employee.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(employee_db, key, value)

        db.commit()
        db.refresh(employee_db)

        return employee_db

    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Failed to update employee"
        )
