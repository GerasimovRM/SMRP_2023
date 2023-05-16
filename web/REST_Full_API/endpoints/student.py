from typing import List

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from models import StudentIn, StudentOut
from database import get_session, Student
from models.student import StudentsOut

router = APIRouter(prefix="/student", tags=["student"])


@router.get("/{student_id}", response_model=StudentOut)
async def get_one(student_id: int,
                  session: Session = Depends(get_session)):
    student: Student = session.query(Student).get(student_id)
    if student:
        student_dto = StudentOut(**student.__dict__)
        return student_dto
    else:
        raise HTTPException(status_code=404,
                            detail=f"Student with id {student_id} not found!")


@router.get("/get_all", response_model=StudentsOut)
async def get_all():
    session = get_session()
    students: Student = session.query(Student).all()
    students_dto = list(map(lambda student: StudentOut(**student.__dict__), students))
    return StudentsOut(students=students_dto)


@router.post("/", response_model=StudentOut)
async def create_student(student: StudentIn):
    session = get_session()
    orm_student = Student(**student.dict())
    session.add(orm_student)
    print(orm_student.__dict__)
    session.commit()
    print(orm_student.__dict__)
    student_dto = StudentOut(**orm_student.__dict__)
    return student_dto

