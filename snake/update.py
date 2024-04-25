import psycopg2

def update(nickname, score):
    """Обновляет счет пользователя или создает нового пользователя, если он не существует."""
    command = """
        UPDATE scores
        SET user_score =  %s 
        WHERE user_name = %s;
        """
    try:
        with psycopg2.connect( host='localhost', port=5432, database='pp2', user='postgres', password='dariko1102') as conn:
            with conn.cursor() as cur:
                cur.execute(command, (score, nickname))
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)