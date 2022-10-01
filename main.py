from os import wait
import psycopg2

conn = psycopg2.connect(database='customers', user='mac', password='1111')

def create_table():
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT exists Customers(     
            id SERIAL PRIMARY KEY, 
            name VARCHAR (60) not null, 
            surname VARCHAR (60) not null,
            email VARCHAR (60) unique not null
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS Tel(
            id SERIAL PRIMARY KEY,
            number_ VARCHAR (60),
            id_cust INTEGER NOT NULL REFERENCES Customers(id)
        )
        """)
        conn.commit()
    conn.close

def insert(name, surname, email):
    with conn.cursor() as cur:
        cur.execute("""
        INSERT INTO Customers(name, surname, email) 
        VALUES (%s,%s,%s) 
        """, (name, surname, email))
        conn.commit()
    conn.close

def insert(number_, id_cust):
    with conn.cursor() as cur:
        cur.execute("""
        INSERT INTO Tel(number_ , id_cust)
        VALUES(%s,%s)
        """, (number_, id_cust))
        conn.commit()
    conn.close()    

def update(name, surname, email, id=int):
    with conn.cursor() as cur:
        cur.execute("""
        UPDATE Customers SET name=%s, surname=%s, email=%s WHERE id=%s;
        """, (name, surname, email, id))
        conn.commit()
    conn.close()

def delete(id):
    with conn.cursor() as cur:
        cur.execute("""
        DELETE FROM Customers WHERE id=%s
        """, (id))
        conn.commit()
    conn.close()

def select():
    while True:
        date = int(input('\n1-Поиск по имени'
        '\n2-Поиск по фамилии'
        '\n3-Поиск по email'
        '\n4-Поиск по телефону'
        '\nВыберите команду для поика: '))
        if date == 1:
            name = input('Введите имя: ')
            with conn.cursor() as cur:
                cur.execute("""
                SELECT name, surname, email, number_ FROM Customers c
                LEFT JOIN Tel t on c.id = t.id_cust
                WHERE name=%s
                """, (name,))
                print(cur.fetchall())
                break
        elif date == 2:
            surname = input('Введите фамилию: ')
            with conn.cursor() as cur:
                cur.execute("""
                SELECT name, surname, email, number_ FROM Customers c
                LEFT JOIN Tel t on c.id = t.id_cust
                WHERE surname=%s
                """,(surname,))
                print(cur.fetchall())
                break
        elif date == 3:
            email = input('Введите email: ') 
            with conn.cursor() as cur:
                cur.execute("""
                SELECT name, surname, email, number_ FROM Customers c
                LEFT JOIN Tel t on c.id = t.id_cust
                WHERE email=%s
                """,(email,))
                print(cur.fetchall())
                break  
        elif date == 4:
            number_ = input('Введите номер телефона: ')
            with conn.cursor() as cur:
                cur.execute("""
                SELECT name, surname, email, number_ FROM Customers c
                LEFT JOIN Tel t on c.id = t.id_cust
                WHERE number_=%s
                """,(number_,))
                print(cur.fetchall())
                break  
        else:
            print('Не верная команда')        



   