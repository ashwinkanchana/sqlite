import sqlite3


DATABASE_NAME = "database.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def createStudentTable():
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


def printTableDescription():
    db = get_db()
    cursor = db.cursor()
    print("Table description")
    cursor.execute("PRAGMA table_info('student')")
    for row in cursor:
        print(row)


def updateTableSchema():
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        '''
        ALTER TABLE student
        ADD COLUMN marks INT DEFAULT 0;
        '''
    )
    print("Updated table schema")


def dropTable():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DROP TABLE student;")
    print("Table dropped")


def insertData(studentData):
    db = get_db()
    cursor = db.cursor()
    for student in studentData:
        cursor.execute(
            '''
            INSERT INTO student
            (full_name, birth_date)
            VALUES (?, ?);
            ''',
            (student[0], student[1])
        )
    db.commit()
    print("Data inserted")


def updateMarksByID(id, marks):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        '''
        UPDATE student 
        SET marks = ?
        WHERE id = ?;
        ''',
        (marks, id)
    )
    db.commit()
    print("Data updated")


def deleteByID(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        '''
        DELETE FROM student
        WHERE ID = ?;
        ''',
        (id,)
    )
    db.commit()
    print("Data deleted")


def printStudentData():
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


createStudentTable()

printTableDescription()

updateTableSchema()

studentData = [['Murielle Nockles', '2021-06-06'],
               ['Kristoforo Gerrans', '2021-01-10'],
               ['Julius Renfree', '2021-04-22'],
               ['Pippo Prendeguest', '2020-10-03'],
               ['Horatio Peat', '2021-05-04'],
               ]

insertData(studentData)

updateMarksByID(1, 80)

deleteByID(2)

printStudentData()

dropTable()
