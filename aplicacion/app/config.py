import psycopg2
import os

def get_cursor():
    # conn = psycopg2.connect(database=os.environ['OPENSHIFT_APP_NAME'],
    #                         user=os.environ['OPENSHIFT_POSTGRESQL_DB_USERNAME'],
    #                         password=os.environ['OPENSHIFT_POSTGRESQL_DB_PASSWORD'],
    #                         host=os.environ['OPENSHIFT_POSTGRESQL_DB_HOST'],
    #                         port=os.environ['OPENSHIFT_POSTGRESQL_DB_PORT'])
    conn = psycopg2.connect(database='pruebas', user='miguel', password='')
    cursor = conn.cursor()
    return cursor


def close_cursor(cursor):
    conn = cursor.connection
    cursor.close()
    conn.close()
