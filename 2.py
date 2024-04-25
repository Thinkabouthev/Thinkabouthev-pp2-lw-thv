import psycopg2
import csv

def insert_from_csv(filename):
    conn = psycopg2.connect(
        host='localhost',
        port=5432,
        database='pp2',
        user='postgres',
        password='dariko1102'
)
    cursor = conn.cursor()

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            cursor.execute(
                "INSERT INTO phoneBook (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
                (row[0], row[1], row[2])
            )

    conn.commit()
    cursor.close()
    conn.close()


insert_from_csv('data.csv')


'''Implement two ways of inserting data into the PhoneBook.
upload data from csv file
entering user name, phone from console'''