from flask import (
    Blueprint, send_from_directory
)

bp = Blueprint('web_app_bp', __name__)

@bp.route('/', defaults={'path': ''})
@bp.route('/<path:path>')
def index(path):
    return send_from_directory('web/web','index.html')