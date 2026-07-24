from fastapi import FastAPI, status

app=FastAPI(
    title='My First FastApi Project',
    description='FAstApi project made by Abdul Hanan',
    version='1.0.0'
)

@app.get(
    '/',
    status_code=status.HTTP_200_OK,
    tags=['General'],
)
def root() -> dict[str,str]:
    return {
        'message':'Welcome to FastApi BAckend Foundations'
    }

@app.get(
    '/health',
    status_code=status.HTTP_200_OK,
    tags=['General']

)
def health_checker() -> dict[str,str]:
    return {
        'status' : 'healthy'
    }

# One Path parameter
@app.get(
     '/students/{student_id}',
     status_code=status.HTTP_200_OK,
     tags=['Students']
)
def get_student(student_id:int) -> dict[str,int|str]:
    return {
        'student_id':student_id,
        'message':"Hello Hanan"

    }


# one query parameter
@app.get(
    '/search',
    status_code=status.HTTP_200_OK,
    tags='Search'
)
def search_student(keyword:str) -> dict[str,str]:
    return {
        'keyword':keyword,
        'message':'FastApi is server'

    }


