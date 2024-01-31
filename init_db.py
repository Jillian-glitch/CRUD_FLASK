import psycopg2

conn = psycopg2.connect(database="postgres", host="localhost", user="postgres", password="6338", port="5432")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS courses (id serial PRIMARY KEY, name varchar(100), fees integer)""")
cur.execute("""INSERT INTO courses(name,fees,duration) VALUES ('python', 6500, 45), ('java', 4500, 40), ('Angular', 3000, 70)""")


conn.commit()
cur.close()
conn.close()
