from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from database.base_meta import Base


class Student(Base):
    __tablename__ = 'Student'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(Text(100), nullable=False)
    bdate = Column(Text(10), nullable=False)
    school_id = Column(ForeignKey('School.id'), nullable=False)

    school = relationship('School')

    def __str__(self):
        return f"Студент {self.id}: {self.name} {self.bdate}"