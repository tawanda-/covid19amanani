from flask import (
    Blueprint, send_from_directory
)

bp = Blueprint('web_app_bp', __name__)

@bp.route('/')
def index():
    return send_from_directory('web/web','index.html')