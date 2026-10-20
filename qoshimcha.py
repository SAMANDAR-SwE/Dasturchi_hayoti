import os
import psycopg2
from dotenv import load_dotenv


load_dotenv()


def main():
    connection = None
    try:
        connection = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        with connection.cursor() as cursor:
            cursor.execute("SELECT version();")
            print(cursor.fetchone())

        cursor = connection.cursor()

    # Main rancode















    # Erorr code
    except (Exception, psycopg2.Error) as error:
        print("Xatolik yuz berdi:", error)
        if connection:
            connection.rollback()
    
    # Connection STOP
    finally:
        if 'connection' in locals() and connection:
            cursor.close()
            connection.close()
            print("\nPostgreSQL ulanishi yopildi.")


if __name__ == "__main__":
    main()