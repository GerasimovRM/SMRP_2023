from fastapi import APIRouter
from sqlalchemy.orm import create_session

from web.REST_Full_API.models import StudentIn, StudentOut
from web.REST_Full_API.database import get_session, Student

router = APIRouter(prefix="/student", tags=["student"])


@router.get("/{student_id}", response_model=StudentOut)
async def get_one(student_id: int):
    session = create_session()
    student: Student = session.query(Student).get(student_id)
    print(student.__dict__)