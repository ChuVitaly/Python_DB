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


    # Телефон для существующего клиента
    def add_phone(CustomerId, PhoneNumber):
        cur.execute("""
                    INSERT INTO phone(CustomerId, PhoneNumber) VALUES(%s, %s);
                """, (CustomerId, PhoneNumber))
        conn.commit()


    # Меняем данные о клиенте
    def update_customer(CustomerId, Name, LastName, Email):
        sql_update = """ UPDATE customers
                            SET Name = %s, LastName = %s, Email = %s                   
                            WHERE CustomerId = %s """
        cur.execute(sql_update, (Name, LastName, Email, CustomerId))
        conn.commit()

    #  удалить телефон для существующего клиента
    def delete_phone(CustomerId):
        cur.execute("DELETE FROM phone WHERE PhoneId = %s", (CustomerId,))
        conn.commit()


    # delete_phone(4)
    # create_tables()
    # add_new_customer(cur, 'Nick', 'Mull', 'g12131@mail.ru', '8921337859')
    # add_phone(4, '674870000000')
    # update_customer(5, 'Simon', 'Duhov', 'sima@noll.rom')

conn.close()
