'''
    Country blueprint

    routes: 
        /country/ For all countries get the latest data {deaths, confirmed, vaccinated}
        /country/<iso2> - get this country ref:<iso2>  latest data {deaths, confirmed, vaccinated}
        /country/<iso2>/daily - get this country ref:<iso2>  all time the historical daily data
        /country/<iso2>/daily?from=[ddmmyy],to=[ddmmyy] - get this country ref:<iso2>  daily data within range, 
        if range out of bounds no data is returned
        /country/all/percapita - get per capita values (deaths, confirmed, vaccinated) for all countries
        /country/<iso2>/percapita - get per capita for this country ref:<iso2> (deaths, confirmed, vaccinated)
'''

from flask import( Blueprint, jsonify)

bp = Blueprint("country", __name__, url_prefix='/country')

@bp.route('/')
def index(iso2):
    return

@bp.route('/<iso2>')
def country(iso2):
    return

@bp.route('/<iso2>/percapita')
def percapita(iso2):
    return

@bp.route('/<iso2>/daily')
def daily(iso2):
    return
    
@bp.route('/test')
def test():
    result = {'hello':'world'}
    return jsonify(result)