import psycopg2
import csv

conn = psycopg2.connect(
    host='localhost',
    port=5432,
    database='pp2',
    user='postgres',
    password='dariko1102'
)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Phonebook(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone_phone_number VARCHAR(11)
    );  
            """)
conn.commit()

def update(sn, mode, newv):
    cur.execute("""UPDATE phonebook
    SET {} = '{}'
    WHERE last_name = '{}'
    """.format(mode, newv, sn))
    conn.commit()

def delete(sn):
    cur.execute("""DELETE FROM Phonebook
    WHERE last_name='{}'
    """.format(sn))
    conn.commit()

#entering user name, phone from console

mode = "enter"
while True:
    print("Type 'enter' if you want to add more data and type 'stop' to break")
    mode = input()
    if mode == "stop":
        break
    mytuple = []
    print("enter first_name:")
    mytuple.append(input())
    print("enter last_name:")
    mytuple.append(input())
    print("enter phone_phone_number:")
    mytuple.append(input())
    mytuple = tuple(mytuple)
    cur.execute("""INSERT INTO phonebook (first_name, last_name, phone_number) VALUES
    {};
    """.format(mytuple))
    conn.commit()

while True:
    mode = input()
    with open(mode + '.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute("INSERT INTO phonebook VALUES (%s,%s,%s)", row)
            conn.commit()

#Implement updating data in the table (change user first name or phone)
while True:
    print("Type 'update' to update some data or 'stop' to break")
    mode = input()
    if mode == "stop":
        break
    cur.execute("""SELECT * FROM phonebook""")
    print(cur.fetchall())
    print("Enter last_name")
    idtochange = input()
    print("What you want to change? name/phone_number")
    mode = input()
    print("Enter new name/phone_number")
    newvalue = input()
    update(idtochange, mode, newvalue)

# DELETING DATA-----------
while True:
    print("want to delete some data? yes/no")
    mode = input()
    if mode == "no":
        break
    cur.execute("""SELECT * FROM phonebook""")
    print(cur.fetchall())
    print("Enter last_name")
    idtodelete = input()
    delete(idtodelete)
    conn.commit()

cur.close()
conn.close()