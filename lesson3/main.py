from database import School, Student, create_session, global_init


global_init("database/db.db")
session = create_session()
# создание нового студента
# new_student = Student(name="Денис Фролов",
#                       bdate="04.01.2005",
#                       school_id=2)
# session.add(new_student)
# session.commit()

# обновить студента
# old_student = session.query(Student).filter(Student.id == 7).first()
# print(old_student)
# old_student.bdate = '04.01.2007'
# session.commit()

# удаление студента
# old_student = session.query(Student).filter(Student.id == 7).first()
# session.delete(old_student)
# session.commit()


# достать всех студентов
students = session.query(Student).all()
for student in students:
    print(student)


students = session.query(Student).filter(Student.name.like("П%"), Student.bdate.like("23%"))
for student in students:
    print(student, student.school)


