'''
    Create database connection
    Initialise database
'''

import psycopg
from flask import current_app, g

def get_db(autocommit=False):
    if 'db' not in g:
        g.db = psycopg.connect(
                            host='localhost',
                            dbname='covid19-amanani',
                            user='postgres',
                            password='tawanda',
                            autocommit=autocommit)

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()