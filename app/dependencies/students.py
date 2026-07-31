from app.services.student_service import StudentService

student_service=StudentService()


def get_student_service() -> StudentService:
    return student_service