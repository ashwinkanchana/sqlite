from utils.db import get_db


def drop_student_table():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DROP TABLE student;")
    db.commit()
    print("Table dropped")


def delete_by_id(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        '''
        DELETE FROM student
        WHERE ID = {};
        '''.format(id))
    db.commit()
    print("Data deleted")