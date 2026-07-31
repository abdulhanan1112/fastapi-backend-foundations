from enum import Enum
from pydantic import BaseModel,Field


class Program(str,Enum):
    Software_Engineering='software_engineering'
    Computer_Science='computer_science'
    Informational_Technology='informational_technology'




class Address(BaseModel):
    city:str = Field(
        min_length=2,
        max_length=20
    )
    country:str = Field(
        min_length=2,
        max_length=20
    )




# class to create Student
class StudentCreate(BaseModel):
    name:str = Field(
        min_length=2,
        max_length=100
    )
    age:int = Field(
        ge=15,
        le=100
    )
    email:str|None = Field(
        default = None,
        max_length=120
    )
    program:Program
    address:Address            # nested pydantic model




# Student Response pydantic model
class StudentResponse(BaseModel):
    id : int
    name : str
    age : int
    email : str | None
    program:Program
    address:Address