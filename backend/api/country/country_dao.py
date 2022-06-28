import psycopg
from psycopg.rows import dict_row

from .. import db

def get_country_data(iso):

    if iso == 'ALL':
        with db.get_db().cursor(row_factory=dict_row) as cursr:
            cursr.execute("""
                SELECT *
                FROM current_data
                INNER JOIN country ON current_data.iso=country.iso
            """)
            return cursr.fetchall()
    else:
        with db.get_db().cursor(row_factory=dict_row) as cursr:
            cursr.execute("""
                SELECT *
                FROM current_data
                INNER JOIN country ON current_data.iso=country.iso
                WHERE current_data.iso = %s;
            """, (iso,))
            return cursr.fetchone()    

def get_percapita(iso):

    match iso:
        case 'ALL':
           return _get_all_percapita()
        case _:
            return _get_country_percapita(iso)

def _get_country_percapita(iso):
    with db.get_db().cursor(row_factory=dict_row) as cur:
        cur.execute("""
            SELECT * ,country.population
            FROM current_data
            INNER JOIN country ON current_data.iso=country.iso
            WHERE current_data.iso = %s;
        """, (iso,))

        row = cur.fetchone()
        population = row.get('population')
        country = str(row.get('country')).strip()
        vaxed = row.get('people_vaccinated')/population
        vaxed = row.get('people_vaccinated')/population
        confirmed = row.get('confirmed')/population
        deaths =row.get('deaths')/population

        result = [['country','vaccinated','confirmed', 'deaths']]
        result.append((country, vaxed, confirmed, deaths))
        return result

def _get_all_percapita():
    with db.get_db().cursor(row_factory=dict_row) as cursr:
        cursr.execute("""
            SELECT *
            FROM current_data
            INNER JOIN country ON current_data.iso=country.iso;
        """)
        rows = cursr.fetchall()
        result = [['country','vaccinated','confirmed', 'deaths']]
        for k in rows:
            population = k.get('population')
            country = str(k.get('country')).strip()
            vaxed = k.get('people_vaccinated')/population
            vaxed = k.get('people_vaccinated')/population
            confirmed = k.get('confirmed')/population
            deaths =k.get('deaths')/population
            result.append([country, vaxed, confirmed, deaths])
        return result