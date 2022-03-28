import psycopg2
import psycopg2.extras

from os import getenv
from dotenv import load_dotenv


def get_connection_string():
    load_dotenv()

    user_name = getenv("PSQL_USER")
    password = getenv("PSQL_PASSWORD")
    host = getenv("PSQL_HOST")
    database_name = getenv("PSQL_DATABASE")

    env_variables_defined = user_name and password and host and database_name

    if env_variables_defined:
        return f"postgresql://{user_name}:{password}@{host}/{database_name}"
    else:
        raise KeyError("Some necessary environment variable(s) are not defined")


def open_database():
    try:
        connection_string = get_connection_string()
        connection = psycopg2.connect(connection_string)
        connection.autocommit = True
    except psycopg2.DatabaseError as exception:
        print("Database connection problem")
        raise exception
    return connection


def connection_handler(function):
    def wrapper(*args, **kwargs):
        connection = open_database()
        
        dict_cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        ret_value = function(dict_cur, *args, **kwargs)
        dict_cur.close()
        connection.close()
        return ret_value

    return wrapper
