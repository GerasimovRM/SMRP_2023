from lesson3.database import global_init, create_session, Parent, Student, ParentStudent


global_init("./database/db.db")
session = create_session()

# parents = session.query(Parent).all()
# for parent in parents:
#     for obj in parent.students:
#         print(obj.student, obj.parent)

parent = Parent(name="Родитель Пупы Лупина")
session.add(parent)
session.commit()
parent_student = ParentStudent(parent_id=parent.id,
                               student_id=4)
session.add(parent_student)
session.commit()
