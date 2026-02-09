from datetime import date
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel



class Request(SQLModel, table=True):
    num : Optional[int] = Field(default=None, primary_key=True)
    employee_id : Optional[int] = Field(foreign_key="employee.id")
    date : date
    equipment : str
    type : str
    description : str
    client : str
    employee_name : Optional[str] = None
    status : str = "awaiting"

    employee : Optional["Employee"] = Relationship(back_populates="requests")

class Employee(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    name : str

    requests : List[Request] = Relationship(back_populates="employee")