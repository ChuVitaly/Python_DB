import psycopg2

conn = psycopg2.connect(database="customer_db", user="postgres", password="583410")
with conn.cursor() as cur:
    # удаление таблиц
    # cur.execute("""
    # DROP TABLE homework;
    # DROP TABLE course;
    # """)

    # Создание таблицы

    cur.execute("""
    CREATE TABLE IF NOT EXISTS customers(
        id SERIAL PRIMARY KEY,
        name VARCHAR(40),
        lastname VARCHAR(60) NOT NULL,
        email VARCHAR(40) NOT NULL,
        phone VARCHAR(40)
    );
    """)

    # conn.commit()

conn.close()
