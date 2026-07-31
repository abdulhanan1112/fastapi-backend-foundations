
class StudentError(Exception):
    """Base Exception for student related errors"""

    pass


class StudentNotFoundError(StudentError):
    def __init__(self,student_id : int) -> None:
        self.student_id=student_id

        super().__init__(
            f"Student with id {student_id} is not found"
        )



class DuplicateStudentEmailError(StudentError):
    def __init__(self,email:str) -> None:
        self.email=email
        
        super().__init__(
            f"A student with this email {email} is already exist"
        )    
