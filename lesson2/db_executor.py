import sqlite3

connection = sqlite3.connect("db.db")
cursor = connection.cursor()
name = 'Никита Иглин'
bdate = '03.11.2002'
school_id = 2
query = cursor.execute(f"""INSERT INTO Student (name, bdate, school_id)
                            VALUES ('{name}', '{bdate}', {school_id})""")
connection.commit()
query = cursor.execute("SELECT * FROM Student")
result = query.fetchall()

print(*result, sep='\n')