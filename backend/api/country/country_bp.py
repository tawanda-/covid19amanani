'''
    Country blueprint
'''

from flask import( Blueprint, jsonify)

bp = Blueprint("country", __name__, url_prefix='/country')

@bp.route('/test')
def test():
    result = {'hello':'world'}
    return jsonify(result)