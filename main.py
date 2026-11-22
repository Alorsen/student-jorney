import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    major TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses( 
    course_id INTEGER PRIMARY KEY AUTOINCREMENT
    course_name TEXT
    instructor TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students_courses(
    student_id INTGER,
    course_id INTEGER,
    FOREIGN KEY(course_id) REFERENCES students(id) ON DELETE CASCADE
    FOREIGN KEY(course_id) REFERENCES courses (courses_id) ON DELETE CASCADE
    PRIMARY KEY(student_id, course_id)     
)
""")


conn.commit()
conn.close()