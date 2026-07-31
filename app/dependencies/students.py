from app.services.student_service import StudentService
from app.repositories.student_repository import InMemoryStudentRepository

student_repository=InMemoryStudentRepository()

student_service=StudentService(student_repository)


def get_student_service() -> StudentService:
    return student_service