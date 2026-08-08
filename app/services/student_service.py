
from app.repositories.student_repository import InMemoryStudentRepository
from app.core.exceptions import (
    StudentNotFoundError,
    DuplicateStudentEmailError
)
from app.schemas.student import StudentCreate
import logging

logger=logging.getLogger(__name__)

class StudentService:
    def __init__(self,repository:InMemoryStudentRepository):
        self.repository=repository


    def create_student(self,student_data: StudentCreate) -> dict[str,object]:
        
        student= self.repository.create(student_data.model_dump())
        logger.info(
            "student created student id=%s",
            student["id"]
        )
        return student

    def list_students(self) -> list[dict[str,object]]:
        students = self.repository.list_all()
        logger.debug(
            "students_listed count =%s",
            len(students)
        )
        return students

    
    def get_student_by_id(self,student_id:int) -> dict[str,object]:
        student=self.repository.get_by_id(student_id)
        if student is None:
            logger.warning(
                "student not found with student_id =%s",
                student_id
            )
            raise StudentNotFoundError(student_id)
        
        return student
        

    def update_student(self,student_id:int,student_data : StudentCreate) -> dict[str,object]:
        student = self.repository.update(student_id,student_data.model_dump())
        if student is None:
            logger.warning(
                "Student not found with student_id =%s",
                student_id
            )
            raise StudentNotFoundError(student_id)
        logger.info(
           "student update with student_id =%s",
           student_id 
        )
        return student

    def delete_student(self,student_id : int) -> None:
        is_student_delete=self.repository.delete(student_id)
        if not is_student_delete:
            logger.warning(
                "student is not deleted with student id =%s",
                student_id
            )
            raise StudentNotFoundError(student_id)

        logger.info(
            "student is successfully deleted with student id =%s",
            student_id
        )

