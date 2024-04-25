import psycopg2

def create_tables():
    
    commands = (
        """
        CREATE TABLE IF NOT EXISTS snake_game (
                id SERIAL PRIMARY KEY,
                user_name VARCHAR(30) NOT NULL UNIQUE,
                user_score INT
            );""")
    
    try:
        with psycopg2.connect( host='localhost', port=5432, database='pp2', user='postgres', password='dariko1102') as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

