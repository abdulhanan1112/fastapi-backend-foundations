from fastapi import FastAPI, status
from fastapi import Path,Query
from enum import Enum
from pydantic import BaseModel


class Program(str,Enum):
    Software_Engineering='software_engineering'
    Computer_Science='computer_science'
    Informational_Technology='informational_technology'


# class to create Student
class StudentCreate(BaseModel):
    name:str
    age:int
    email:str|None = None
    program:Program


students=[]

app=FastAPI(
    title='Student API',
    version='1.0.0'
)


# create Student endpoint
@app.post(
    '/students',
    status_code=status.HTTP_201_CREATED,
    tags=['Students']
)
def student(student_data:StudentCreate) -> dict[str,object]:
    student_id=len(students)+1
    new_student={
        "id":student_id,
        **student_data.model_dump()
    }
    students.append(new_student)
    return new_student

# Get student endpoint in which there is also filteration of program, age, limit
@app.get(
    '/students',
    status_code=status.HTTP_200_OK,
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
    return result


# get student by student id
@app.get(
    '/students/{student_id}',
    status_code=status.HTTP_200_OK,
    tags=['Students']
)
def get_students(student_id:int) -> dict[str,object]:
    return students[student_id-1]






