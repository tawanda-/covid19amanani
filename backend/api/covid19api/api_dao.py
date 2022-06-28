from .. import db

def insert(type, data):

    match type:
        case 'latest':
            _insert_country(data)
        case 'vaccine':
            _insert_vaccine(data)
        case 'history':
            _insert_history(data)
        case _:
            return

'''
    Insert data into country annd status table
'''
def _insert_country(data):

    dbase = db.get_db()

    status_list = []

    try:
        with dbase.cursor().copy(db.COPY_COUNTRY) as copy:     
            for k, v in data.items():
                country = v.get("All")            
                status = (country.get('abbreviation'),country.get('confirmed'),country.get('deaths'),0,0,0)
                status_list.append(status)
                copy.write_row(
                    (country.get('abbreviation'),country.get('country'),country.get('population'),country.get('life_expectancy'),country.get('continent'),country.get('location'),country.get('capital_city'))
                )

        with dbase.cursor().copy(db.COPY_CURRENT_DATA) as copy:     
            for k in status_list:
                copy.write_row(k)

    except:
        dbase.rollback()
    else:
        dbase.commit()

'''
    Method will try to insert data into status table, 
    if the row already exists then try to update the row.
'''
def _insert_vaccine(data):

    dbase = db.get_db()

    try:
        with dbase.cursor() as cursr:     
            for k, v in data.items():
                country = v.get("All")  
                status = (country.get('abbreviation'),0,0,country.get('administered'),country.get('people_vaccinated'),
                            country.get('people_partially_vaccinated'))
                cursr.execute("""
                    INSERT INTO current_data (iso, confirmed, deaths, administered, people_vaccinated, people_partially_vaccinated)
                    VALUES (%s,%s,%s,%s,%s,%s)
                    ON CONFLICT (iso) DO UPDATE SET 
                        administered = EXCLUDED.administered, 
                        people_vaccinated = EXCLUDED.people_vaccinated, 
                        people_partially_vaccinated = EXCLUDED.people_partially_vaccinated;
                """, status)
    except:
        dbase.rollback()
    else:
        dbase.commit()

'''
    Insert data into daily_numbers table
'''
def _insert_history(data):
    return