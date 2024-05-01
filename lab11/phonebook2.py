import psycopg2

def connect_to_db():
    try:
        conn = psycopg2.connect(
            host='localhost',
            port=5432,
            database='pp2',
            user='postgres',
            password=''
        )
        print("Connected to the database")
        return conn
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)

def create_table(conn):
    try:
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS Phonebook(
                        id SERIAL PRIMARY KEY,
                        first_name VARCHAR(50),
                        last_name VARCHAR(50),
                        phone_number VARCHAR(11)
                    );""")
        conn.commit()
        print("PhoneBook table created successfully")
    except psycopg2.Error as e:
        print("Error creating PhoneBook table:", e)

def insert_data(conn, first_name, last_name, phone_number):
    try:
        cur = conn.cursor()
        cur.execute("""INSERT INTO Phonebook (first_name, last_name, phone_number)
                        VALUES (%s, %s, %s);""", (first_name, last_name, phone_number))
        conn.commit()
        print("Data inserted successfully")
    except psycopg2.Error as e:
        print("Error inserting data:", e)

def update_data(conn, user_id, first_name=None, last_name=None, phone_number=None):
    try:
        cur = conn.cursor()
        update_query = "UPDATE Phonebook SET "
        update_values = []

        if first_name:
            update_query += "first_name = %s, "
            update_values.append(first_name)
        if last_name:
            update_query += "last_name = %s, "
            update_values.append(last_name)
        if phone_number:
            update_query += "phone_number = %s, "
            update_values.append(phone_number)

        update_query = update_query.rstrip(", ") + " WHERE id = %s;"
        update_values.append(user_id)

        cur.execute(update_query, update_values)
        conn.commit()
        print("Data updated successfully")
    except psycopg2.Error as e:
        print("Error updating data:", e)


def delete_data_by_firstname(conn, first_name):
    try:
        cur = conn.cursor()
        delete_query = "DELETE FROM Phonebook WHERE first_name = %s;"
        cur.execute(delete_query, (first_name,))
        conn.commit()
        print("Data deleted successfully")
    except psycopg2.Error as e:
        print("Error deleting data:", e)

def query_data(conn, pattern):
    try:
        cur = conn.cursor()
        cur.execute("""SELECT * FROM Phonebook
                       WHERE first_name ILIKE %s 
                          OR last_name ILIKE %s
                          OR phone_number ILIKE %s""", (f'%{pattern}%', f'%{pattern}%', f'%{pattern}%'))
        rows = cur.fetchall()
        if rows:
            print("Query results:")
            for row in rows:
                print(row)
        else:
            print("No data found.")
    except psycopg2.Error as e:
        print("Error querying data:", e)
#NEW Functions

def insert_or_update_user(conn, first_name, phone_number):
    try:
        cur = conn.cursor()
        cur.execute("""SELECT id FROM Phonebook WHERE first_name = %s""", (first_name,))
        user_id = cur.fetchone()
        if user_id:
            update_data(conn, user_id[0], phone_number=phone_number)
        else:
            insert_data(conn, first_name, None, phone_number)
    except psycopg2.Error as e:
        print("Error inserting or updating user:", e)

def insert_users_bulk(conn, users_data):
    try:
        cur = conn.cursor()
        for user_data in users_data:
            if len(user_data) == 2 and len(user_data[1]) == 11:  # Assuming phone number length should be 11
                insert_data(conn, user_data[0], None, user_data[1])
            else:
                print("Incorrect data:", user_data)
    except psycopg2.Error as e:
        print("Error inserting users in bulk:", e)

def get_users_with_pagination(conn, limit_rows, offset_rows):
    try:
        cur = conn.cursor()
        cur.execute("""SELECT * FROM Phonebook LIMIT %s OFFSET %s""", (limit_rows, offset_rows))
        rows = cur.fetchall()
        if rows:
            print("Query results:")
            for row in rows:
                print(row)
        else:
            print("No data found.")
    except psycopg2.Error as e:
        print("Error querying data with pagination:", e)

def delete_data_by_username_or_phone(conn, value):
    try:
        cur = conn.cursor()
        cur.execute("""DELETE FROM Phonebook WHERE first_name = %s OR phone_number = %s""", (value, value))
        conn.commit()
        print("Data deleted successfully")
    except psycopg2.Error as e:
        print("Error deleting data:", e)

def main():
    conn = connect_to_db()
    create_table(conn)
    
    while True:
        print("\nChoose action:")
        print("1. Insert data")
        print("2. Update data")
        print("3. Delete data")
        print("4. Query data")
        print("5. Insert or update user")
        print("6. Insert users in bulk")
        print("7. Query data with pagination")
        print("8. Delete data by username or phone")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            phone_number = input("Enter phone number: ")
            insert_data(conn, first_name, last_name, phone_number)
        elif choice == "2":
            user_id = input("Enter user ID to update: ")
            first_name = input("Enter new first name (leave empty to skip): ")
            last_name = input("Enter new last name (leave empty to skip): ")
            phone_number = input("Enter new phone number (leave empty to skip): ")
            update_data(conn, user_id, first_name, last_name, phone_number)
        elif choice == "3":
            first_name = input("Enter first name to delete data: ")
            delete_data_by_firstname(conn, first_name)
        elif choice == "4":
            pattern = input("Enter search pattern: ")
            query_data(conn, pattern)
        elif choice == "5":
            first_name = input("Enter first name: ")
            phone_number = input("Enter phone number: ")
            insert_or_update_user(conn, first_name, phone_number)
        elif choice == "6":
            users_data = []
            while True:
                first_name = input("Enter first name (or type 'done' to finish): ")
                if first_name.lower() == 'done':
                    break
                phone_number = input("Enter phone number: ")
                users_data.append((first_name, phone_number))
            insert_users_bulk(conn, users_data)
        elif choice == "7":
            limit_rows = int(input("Enter limit of rows: "))
            offset_rows = int(input("Enter offset of rows: "))
            get_users_with_pagination(conn, limit_rows, offset_rows)
        elif choice == "8":
            value = input("Enter username or phone number to delete data: ")
            delete_data_by_username_or_phone(conn, value)
        elif choice == "9":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again")

    conn.close()

if __name__ == "__main__":
    main()
