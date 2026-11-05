
import pytest
from pydantic import ValidationError
from schemas import Employee


def test_valid_employee():
    employee = Employee(name="  Ping  ", age=25)

    assert employee.name == "Ping"
    assert employee.age == 25


def test_reject_blank_name():
    with pytest.raises(ValidationError):
        Employee(name="   ", age=25)


def test_reject_negative_age():
    with pytest.raises(ValidationError):
        Employee(name="Ping", age=-5)
