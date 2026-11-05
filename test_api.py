
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_employee_not_found():
    response = client.get("/employees/999999999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Employee not found"}


def test_create_employee_invalid_age():
    response = client.post(
        "/employees",
        json={"name": "PingTest", "age": -5}
    )

    assert response.status_code == 422


def test_get_employees_over_25():
    response = client.get("/employees/over-25")

    assert response.status_code == 200

    employees = response.json()

    for employee in employees:
        assert employee["age"] > 25
