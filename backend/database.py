import psycopg2 
from config import host, user, password, db_name, port

connection = psycopg2.connect(
    host = host,
    user = user,
    password = password,
    database = db_name,
    port = port
)
connection.autocommit = True
with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE Paintings(
                id serial PRIMARY KEY,
                name varchar(40) NOT NULL,
                photo varchar(100) NOT NULL,
                author varchar(40) NOT NULL,
                price integer NOT NULL);"""
        )
        print(f"print db created!")


# try:
#     connection = psycopg2.connect(
#         host = host,
#         user = user,
#         password = password,
#         database = db_name,
#         port = port
#     )

#     with connection.cursor() as cursor:
#         cursor.execute(
#             "SELECT VERSION();"
#         )

#         print(f"Server version: {cursor.fetchone()}")
# except Exception as e:
#     print(f"error {e}")
# finally:
#     if connection:
#         connection.close()
#         print(f"Connection closed")


