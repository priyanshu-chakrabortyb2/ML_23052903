import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="Priyanshu@3004",
    database="ALPHA",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)

with conn:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM students;")
        rows = cur.fetchall()
        for r in rows:
            print(r)
