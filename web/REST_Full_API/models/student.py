from typing import List

from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from database import Student

StudentOut = sqlalchemy_to_pydantic(Student)


class StudentIn(sqlalchemy_to_pydantic(Student)):
    class Config:
        orm_mode = True


StudentIn.__fields__.pop('id')
print(StudentIn.__fields__)


class StudentsOut(BaseModel):
    students: List[StudentOut]
