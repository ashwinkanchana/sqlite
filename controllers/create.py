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


def insert_data(studentData):
    db = get_db()
    cursor = db.cursor()
    for student in studentData:
        cursor.execute(
            '''INSERT INTO student 
            (full_name, birth_date) 
            VALUES ('{student[0]}', '{student[1]}');''')
    db.commit()
    print("Data inserted")