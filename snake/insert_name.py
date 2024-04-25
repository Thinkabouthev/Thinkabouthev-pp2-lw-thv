import psycopg2

def insert_data(nickname):
    """Вставка данных в таблицу."""
    data = (nickname, 0)
    command = """
        INSERT INTO scores(user_name, user_score) 
        VALUES(%s, %s)
        """
    try:
        with psycopg2.connect(host='localhost', port=5432, database='pp2', user='postgres', password='dariko1102' as conn:
            with conn.cursor() as cur:
                cur.execute(command, data)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)