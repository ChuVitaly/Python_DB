import psycopg2

conn = psycopg2.connect(database="customer_db", user="postgres", password="583410")
with conn.cursor() as cur:
    cur.execute("CREATE TABLE test(id SERIAL PRIMARY KEY);")
    # conn.commit()

conn.close()