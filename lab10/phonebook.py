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

def query_data(conn, filter_by=None, filter_value=None):
    try:
        cur = conn.cursor()
        if filter_by and filter_value:
            query = f"SELECT * FROM Phonebook WHERE {filter_by} = %s;"
            cur.execute(query, (filter_value,))
        else:
            cur.execute("SELECT * FROM Phonebook;")
        rows = cur.fetchall()
        if rows:
            print("Query results:")
            for row in rows:
                print(row)
        else:
            print("No data found.")
    except psycopg2.Error as e:
        print("Error querying data:", e)
    except psycopg2.ProgrammingError as e:
        print("Error in SQL query:", e)


def main():
    conn = connect_to_db()
    create_table(conn)
    
    while True:
        print("\nChoose action:")
        print("1. Insert data")
        print("2. Update data")
        print("3. Delete data")
        print("4. Query data")
        print("5. Exit")
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
            filter_by = input("Enter column name to filter by (leave empty to retrieve all data): ")
            filter_value = input("Enter filter value: ")
            query_data(conn, filter_by, filter_value)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again")

    conn.close()

if __name__ == "__main__":
    main()
