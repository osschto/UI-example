from datetime import date
from typing import List, Optional

from sqlmodel import Field, SQLModel


class Request(SQLModel, table=True):
    num : Optional[int] = Field(default=None, primary_key=True)
    date : date
    equipment : str
    type : str
    description : str
    client : str
    responsible : Optional[str] = None
    status : str = "awaiting"

class Employee(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    name : str