'''
    Create database connection
    Initialise database
'''

import psycopg
import click
from flask import current_app, g
from flask.cli import with_appcontext

COPY_COUNTRY = "COPY country (iso,country,population,life_expectancy,continent,location,capital_city) FROM STDIN"
COPY_CURRENT_DATA = "COPY current_data (iso, confirmed, deaths, administered, people_vaccinated, people_partially_vaccinated) FROM STDIN"

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

'''
    Add tables to DB
'''
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        cursr = db.cursor()
        cursr.execute(f.read().decode('utf8'))
        db.commit()
        cursr.close()

'''
    Cmd line method to initialise db
'''
@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Database initialised.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
