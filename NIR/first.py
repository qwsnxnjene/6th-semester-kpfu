import sqlite3


con = sqlite3.connect("my.db")
cur = con.cursor()


def create_tables():
    cur.execute("CREATE TABLE exam_type (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(32) NOT NULL DEFAULT \'\');")
    cur.execute("CREATE TABLE subject (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(32) NOT NULL DEFAULT \'\');")
    cur.execute("CREATE TABLE course (id INTEGER PRIMARY KEY AUTOINCREMENT, type_id INTEGER, subject_id INTEGER, "
                "name VARCHAR(32) NOT NULL DEFAULT \'\');")


def fill_tables():
    if any(cur.execute(f"SELECT name FROM sqlite_master WHERE name='{name}'").fetchone() is None for name in
           ['exam_type', 'course', 'subject']):
        create_tables()

    exams = """INSERT INTO exam_type (name) VALUES ('ЕГЭ'), ('ОГЭ'), ('Олимпиада');"""
    cur.execute(exams)

    subjects = """
    INSERT INTO subject (name) VALUES (
    'Информатика'),
    ('Математика'),
    ('Русский язык'),
    ('Физика'),
    ('Английский язык');"""
    cur.execute(subjects)

    courses = """
    INSERT INTO course (type_id, subject_id, name) VALUES
    (1, 1, 'Информатика ЕГЭ Тариф Плюс Октябрь'),
    (1, 2, 'Математика ЕГЭ Тариф Основа Сентябрь'),
    (1, 3, 'Русский язык ЕГЭ Тариф Экстра Июль'),
    (2, 4, 'Физика ОГЭ Тариф Обычный Весь год'),
    (2, 5, 'Английский язык ОГЭ Устная часть'),
    (3, 1, 'Информатика Региональный этап ВСОШ'),
    (3, 3, 'Русский язык Перечневые олимпиады');
    """
    cur.execute(courses)



fill_tables()
res = cur.execute("SELECT name FROM course")
print(res.fetchall())
