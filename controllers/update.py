from utils.db import get_db


def update_table_schema():
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        '''
        ALTER TABLE student
        ADD COLUMN marks INT DEFAULT 0;
        '''
    )
    db.commit()
    print("Updated table schema")


def update_marks_by_id(id, marks):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        '''
        UPDATE student 
        SET marks = {}
        WHERE id = {};
        '''.format(marks, id))
    db.commit()
    print("Data updated")