
from app.dependencies.students import get_student_service
from typing import Annotated
from app.services.student_service import StudentService
from fastapi import  status
from app.schemas.student import StudentResponse
from app.schemas.student import StudentCreate
from fastapi import APIRouter,Depends,Path
from app.core.exceptions import StudentNotFoundError
from fastapi import HTTPException


# Api router
router=APIRouter(
    prefix = '/students',
    tags=['Students']
)

# dependency of Students Service
StudentServiceDependency = Annotated[
    StudentService,
    Depends(get_student_service)
]

# To create Students database
@router.post(
    '',
    status_code=status.HTTP_201_CREATED,
    response_model=StudentResponse

)
def create_student(student_data : StudentCreate, student_service : StudentServiceDependency) -> dict[str,object]:
    return student_service.create_student(student_data)




# to get all students
@router.get(
    '',
    status_code=status.HTTP_200_OK,
    response_model=list[StudentResponse]
)
def get_all_student(student_service : StudentServiceDependency) ->list[dict[str,object]]:
    return student_service.list_students()


# to get student by id
@router.get(
    '/{student_id}',
    response_model=StudentResponse,
    status_code=status.HTTP_200_OK
)
def get_student_by_id(student_id :Annotated[int,Path(gt=0,lt=500)],student_service : StudentServiceDependency) -> dict[str,object]:
    try:
        return student_service.get_student_by_id(student_id)
    except StudentNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc)
        ) from exc

# @router.put(
#     '/{student_id}',
#     status_code=status.HTTP_200_OK,
#     response_model=StudentResponse
# )        
# def update_student(student_id:int,student_data : StudentCreate,student_service : StudentServiceDependency) -> dict[str,object]:
#     try:
#         return student_service.update_student(student_id,student_data)
#     except StudentNotFoundError as exc:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=str(exc)
#         ) from exc

# to delete student by id
@router.delete(
    '/{student_id}',
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_student(student_id :int, student_service : StudentServiceDependency):
    try:
        student_service.delete_student(student_id)

    except StudentNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc)
        ) from exc    

