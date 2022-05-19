from flask import Blueprint, jsonify, render_template
from flask_restful import Api


common_blueprint = Blueprint('common', __name__)
common_blueprint_api = Api(common_blueprint)

@common_blueprint.route('/')
def index():
    return render_template('index.jinja')
