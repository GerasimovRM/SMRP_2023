from sqlalchemy import Column, Text, Integer

from database.base_meta import Base


class School(Base):
    __tablename__ = 'School'
    __table_args__ = {'extend_existing': True}

    name = Column(Text(100), nullable=False)
    id = Column(Integer, primary_key=True)
    city = Column(Text(100), nullable=False)

    def __str__(self):
        return f"Школа {self.id}: {self.name} в городе {self.city}"