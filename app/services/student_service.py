
from app.repositories.student_repository import InMemoryStudentRepository
from app.core.exceptions import (
    StudentNotFoundError,
    DuplicateStudentEmailError
)
from pydantic import BaseModel
from app.schemas.student import StudentCreate


class StudentService:
    def __init__(self,repository:InMemoryStudentRepository):
        self.repository=repository


    def create_student(self,student_data: StudentCreate) -> dict[str,object]:
        return self.repository.create(student_data.model_dump())
        

    def list_students(self) -> list[dict[str,object]]:
        return self.repository.list_all()

    
    def get_student_by_id(self,student_id:int) -> dict[str,object]:
        student=self.repository.get_by_id(student_id)
        if student is None:
            raise StudentNotFoundError(student_id)
        return student
        

    def update_student(self,student_id:int,student_data : StudentCreate) -> dict[str,object]:
        student = self.repository.update(student_id,student_data.model_dump())
        if student is None:
            raise StudentNotFoundError(student_id)

        return student

    def delete_student(self,student_id : int) -> None:
        isStudentDelete=self.repository.delete(student_id)
        if not isStudentDelete:
            raise StudentNotFoundError(student_id)

