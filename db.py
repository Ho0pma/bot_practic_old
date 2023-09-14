import psycopg2

connection = psycopg2.connect(
    database='postgres',
    user='postgres',
    password='postgres',
    host='db',
    port='5433'
)
print("Database opened successfully!")


async def select_users():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(" select *     "
                           "   from users ")
            row = cursor.fetchall()
            return row
