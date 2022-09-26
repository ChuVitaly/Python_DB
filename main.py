import psycopg2

conn = psycopg2.connect(database="customer_db", user="postgres", password="583410")
with conn.cursor() as cur:
    # удаление таблиц
    # cur.execute("""
    # DROP TABLE homework;
    # DROP TABLE course;
    # """)

    # Создание таблицы
    def create_tables():
        cur.execute("""
        CREATE TABLE IF NOT EXISTS customers(
            CustomerId SERIAL PRIMARY KEY,
            Name VARCHAR(40),
            Lastname VARCHAR(60) NOT NULL,
            Email VARCHAR(40) NOT NULL
        );
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS phone(
            PhoneId PRIMARY KEY,
            CustomerId INT FOREIGN KEY REFERENCES customers(CustomerId),
            PhoneNumber VARCHAR(50)
        );
        """)


    # conn.commit()

conn.close()
