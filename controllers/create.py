from utils.db import get_db


def create_student_table():
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS student(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            birth_date DATE NOT NULL
        );
        '''
    )
    print("Created table")


def insert_data(student_data):
    db = get_db()
    cursor = db.cursor()
    for student in student_data:
        full_name = student[0]
        birth_date = student[1]
        cursor.execute(
            '''INSERT INTO student
            (full_name, birth_date)
            VALUES('{}', '{}'); 
            '''.format(full_name, birth_date)
            # '''INSERT INTO student 
            # (full_name, birth_date) 
            # VALUES ('{full_name}', '{birth_date}');'''
            )
    db.commit()
    print("Data inserted")