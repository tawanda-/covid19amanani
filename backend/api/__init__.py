import os

from flask import Flask
from flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True,static_folder="web/web/static",)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #register cmd line method to initialise db
    from . import db
    db.init_app(app)

    #CORS
    CORS(app, origins=['http://localhost:3000'])
    app.config['CORS_HEADERS'] = 'Content-Type'

    #register cmd line method to get data from covid19 api
    from .covid19api import api_commands
    app.teardown_appcontext(db.close_db)
    app.cli.add_command(api_commands.get_data_command)

    #Register blueprints
    from .web import web_app_bp
    app.register_blueprint(web_app_bp.bp)

    from .country import country_bp
    app.register_blueprint(country_bp.bp)

    return app