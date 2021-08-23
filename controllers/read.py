from utils.db import get_db


def print_table_description():
    db = get_db()
    cursor = db.cursor()
    print("Table description")
    cursor.execute("PRAGMA table_info('{}');".format('student'))
    for row in cursor:
        print(row)


def print_student_data():
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        '''
        SELECT id, full_name, birth_date, marks
        FROM student
        '''
    )
    print("Table data")
    for row in cursor:
        print(row)