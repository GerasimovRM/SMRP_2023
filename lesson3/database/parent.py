from sqlalchemy import Column, Text, Integer
from sqlalchemy.orm import relationship

from .base_meta import Base


class Parent(Base):
    __tablename__ = 'Parent'
    __table_args__ = {'extend_existing': True}

    name = Column(Text, nullable=False)
    id = Column(Integer, primary_key=True)
    phone = Column(Text, nullable=False)

    students = relationship("ParentStudent", back_populates="parent")

    def __str__(self):
        return f"Родитель {self.id}: {self.name}"