from fastapi import FastAPI, status
from fastapi import Path,Query
from enum import Enum
from pydantic import BaseModel,Field
from fastapi import HTTPException
from typing import Annotated



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




students=[]

app=FastAPI(
    title='Student API',
    version='1.0.0'
)


# create Student endpoint
@app.post(
    '/students',
    status_code=status.HTTP_201_CREATED,
    response_model=StudentResponse,
    tags=['Students']
)
def student(student_data:StudentCreate) -> dict[str,object]:
    if student_data.email is not None:
        flag=False
        for student in students:
            if student['email'] == student_data.email:
                flag=True
                break
        if flag:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail='This email is already exist'
            )

    student_id=len(students)+1
    new_student={
        "id":student_id,
        **student_data.model_dump(),
        "internal fields" : "Created by API"
    }
    students.append(new_student)
    return new_student

# Get student endpoint in which there is also filteration of program, age, limit
@app.get(
    '/students',
    status_code=status.HTTP_200_OK,
    response_model=list[StudentResponse],
    tags=['Students']
)
def get_students(
    program:Annotated[Program|None,Query()] = None,
    minimum_age:Annotated[int|None,Query(ge=0)] = None,
    limit:Annotated[int,Query(gt=1,le=100)] = 10

) -> list:
    
    result=students.copy()
    if program is not None:
        result=[
            student
            for student in result
            if student["program"] ==program
        ]
    if minimum_age is not None:
        result=[
            student
            for student in result
            if student["age"] >=minimum_age
        ]
    return result[:limit]    


# search student by name 
@app.get(
    '/students/search',
    status_code=status.HTTP_200_OK,
    response_model=list[StudentResponse],
    tags=['Students']
)
def get_students_by_name(name:Annotated[str,Query(min_length=2,max_length=100)]) -> list:
    result=students.copy()
    name_smaller=name.lower()
    result=[
        student
        for student in result
        if name_smaller in student["name"].lower() 
    ]
    if len(result) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Student with this name is not exist'
        )
    return result


# get student by student id
@app.get(
    '/students/{student_id}',
    status_code=status.HTTP_200_OK,
    response_model=StudentResponse,
    tags=['Students']
)
def get_students(student_id:int) -> dict[str,object]:
    for student in students:
        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student with this id is not exist"
    )





