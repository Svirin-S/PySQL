from os import wait
import psycopg2

with psycopg2.connect(database='customers', user='mac', password='1111') as conn:
    with conn.cursor() as cur:
        def create_table(cur):
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
        create_table(cur)        
            

        def insert(cur, name, surname, email):
                cur.execute("""
                INSERT INTO Customers(name, surname, email) 
                VALUES (%s,%s,%s) 
                """, (name, surname, email))
        insert(cur, "Сергей", "Петров", 'cgcgdgggd@mail.ru')        
        insert(cur, "Максим", "Смирнов", 'kjkkjljl@mail.ru')     


        def insert2(cur,number_, id_cust):
                cur.execute("""
                INSERT INTO Tel(number_ , id_cust)
                VALUES(%s,%s)
                """, (number_, id_cust))
        insert2(cur, '8(999)888-11-22', 1)
        insert2(cur, '8(777)445-78-21', 3) 
               

        def update_NameSurname(cur, name, surname, id=int):
                cur.execute("""
                UPDATE Customers SET name=%s, surname=%s WHERE id=%s;
                """, (name, surname, id))
        update_NameSurname(cur, 'Петр', 'Петров', 3)


        def update_email(cur, email, id=int):
                cur.execute("""
                UPDATE Customers SET email=%s WHERE id=%s;
                """, (email, id))                
        update_email(cur, 'jkhjkjh@mail.ru', 3)


        def update_tel(cur, number_, id):
            cur.execute("""
            UPDATE Tel SET number_=%s WHERE id=%s;
            """, (number_, id))
        update_tel(cur, '8(111)222-34-34', 2)


        def delete(cur, id):
            cur.execute("""
            DELETE FROM Tel WHERE id_cust=%s;
            """, (id,))
            cur.execute("""
            DELETE FROM Customers WHERE id=%s;
            """, (id,))
        delete(cur, 3)        


        def select_Name(cur, name):
            cur.execute("""
            SELECT name, surname, email, number_ FROM Customers c
            LEFT JOIN Tel t on c.id = t.id_cust
            WHERE name=%s
            """, (name,))
            print(cur.fetchall())
        select_Name(cur, 'Сергей')  


        def select_Surame(cur, surname):
            cur.execute("""
            SELECT name, surname, email, number_ FROM Customers c
            LEFT JOIN Tel t on c.id = t.id_cust
            WHERE surname=%s
            """,(surname,))
            print(cur.fetchall())
        select_Surame(cur, 'Петров')          
        

        def select_email(cur, email):  
            cur.execute("""
            SELECT name, surname, email, number_ FROM Customers c
            LEFT JOIN Tel t on c.id = t.id_cust
            WHERE email=%s
            """,(email,))
            print(cur.fetchall())
        select_email(cur, 'cgcgdgggd@mail.ru')       


        def select_Tel(cur, number_):      
            cur.execute("""
            SELECT name, surname, email, number_ FROM Customers c
            LEFT JOIN Tel t on c.id = t.id_cust
            WHERE number_=%s
            """,(number_,))
            print(cur.fetchall())
        select_Tel(cur, '8(999)888-11-22')            
                   



   