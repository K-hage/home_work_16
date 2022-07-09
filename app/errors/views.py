from flask import Blueprint

from utils import NotFoundById

errors_blueprint = Blueprint('errors_blueprint', __name__)


@errors_blueprint.app_errorhandler(NotFoundById)
def page_error_server(e):
    return 'Нет записи с таким ID'
