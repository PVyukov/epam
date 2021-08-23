import psycopg2
import os

params = {
        "host":"db",
        "database":os.environ['POSTGRES_DB'],
        "user":os.environ['POSTGRES_USER'],
        "password":os.environ['POSTGRES_PASSWORD']
        }

def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE greetings (
            greetings_id SERIAL PRIMARY KEY,
            greetings_text VARCHAR(255) NOT NULL
        )
        """,)
    print(type(commands))
    print(commands)
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def db_add_entry(text: str):

    """ insert a new line into the test table """
    command = """INSERT INTO greetings(greetings_text)
             VALUES(%s);"""
    conn = None
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(command, (text,))
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
