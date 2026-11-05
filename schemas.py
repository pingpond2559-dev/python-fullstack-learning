
from pydantic import BaseModel, Field, field_validator, ConfigDict


class Employee(BaseModel):
    name: str = Field(min_length=1)
    age: int = Field(ge=0)

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str):
        value = value.strip()

        if not value:
            raise ValueError("Name cannot be empty")

        return value


class EmployeeResponse(BaseModel):
    id: int
    name: str
    age: int

    model_config = ConfigDict(from_attributes=True)

class EmployeeUpdate(BaseModel):
    name: str | None = None
    age: int | None = Field(default=None, ge=0)
