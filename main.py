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
                LastName VARCHAR(60) NOT NULL,
                Email VARCHAR(40) NOT NULL
            );
            """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS phone(
                PhoneId SERIAL PRIMARY KEY,
                CustomerId INT REFERENCES customers(CustomerId),
                PhoneNumber VARCHAR(50)
            );
            """)
        conn.commit()

    # Заполняем таблицу
    def add_new_customer(cur, Name, LastName, Email, PhoneNumber):
        cur.execute("""
            INSERT INTO customers(Name, LastName, Email) VALUES(%s, %s, %s);
            """, (Name, LastName, Email))

        cur.execute("""
            INSERT INTO phone(PhoneNumber) VALUES(%s);
        """, (PhoneNumber,))
        conn.commit()

    # create_tables()
    # add_new_customer(cur, 'Nick', 'Mull', 'g12131@mail.ru', '8921337859')

conn.close()
