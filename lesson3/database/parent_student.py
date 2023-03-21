from sqlalchemy import Column, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base_meta import Base


class ParentStudent(Base):
    __tablename__ = 'ParentStudent'
    __table_args__ = {'extend_existing': True}

    parent_id = Column(ForeignKey("Parent.id"), primary_key=True)
    student_id = Column(ForeignKey("Student.id"), primary_key=True)

    parent = relationship("Parent", back_populates="students")
    student = relationship("Student", back_populates="parents")


    def __str__(self):
        return f"Школа {self.id}: {self.name} в городе {self.city}"