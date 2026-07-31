
from app.dependencies.students import get_student_service

# Api router
router=APIRouter(
    prefix = '/students',
    tags=['Students']
)

# instance of Students Service
student_service=get_student_service()

# To create Students database
@router.post(
    ''
)
def create(student_data : StudentCreate):
    return student_service.create_student(student_data)





@router.get(
    ''
)