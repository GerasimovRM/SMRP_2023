from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from ..database import Student

StudentOut = sqlalchemy_to_pydantic(Student)
StudentIn = sqlalchemy_to_pydantic(Student)
StudentIn.__fields__.pop('id')
