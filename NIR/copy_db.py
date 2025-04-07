import sqlite3

con = sqlite3.connect('my.db')
cur = con.cursor()


def copy_db():
    res = cur.execute("SELECT * FROM sqlite_master").fetchall()

    con2 = sqlite3.connect('copy.db')
    cur2 = con2.cursor()

    for table in res:
        if 'sqlite_sequence' not in table[-1]:
            print(table[1])
            print(con.execute(f"SELECT * FROM {table[1]}").fetchall())
            if cur2.execute(f"SELECT * FROM sqlite_master WHERE name='{table[1]}'").fetchone() is None:
                cur2.execute(table[-1])

    return cur2


r = copy_db()
res = r.execute('SELECT name FROM course')
print(res.fetchall())