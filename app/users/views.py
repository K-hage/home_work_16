from flask import Blueprint, request, jsonify

from classes.models import User
from app.users.dao.users_dao import UsersDAO
from utils import NotFoundById

users_blueprint = Blueprint('users_blueprint', __name__)


@users_blueprint.route('/', methods=['GET', 'POST'])
def page_users():
    """ Вьюшка:
    GET = все данные пользователей
    POST = добавление данных пользователя из JSON
    """

    if request.method == 'GET':
        users = []
        for user in User.query.all():
            users.append(User.make_dict(user))
        return jsonify(users)

    if request.method == 'POST':
        data = request.json
        new_user = UsersDAO().add_new(data)
        return jsonify(new_user)


@users_blueprint.route('/<int:user_id>/', methods=['GET', 'PUT', 'DELETE'])
def page_update_users(user_id):
    """ Вьюшка:
    GET = данные пользователя по ID
    PUT = обновление данных пользователя из полученного JSON
    DELETE = удаление данных пользователя по ID
    """

    user = User.query.get(user_id)  # ищем пользователя

    if user is None:  # ошибка при отсутствии записи по ID
        raise NotFoundById
    if request.method == 'GET':
        return jsonify(User.make_dict(user))

    if request.method == 'PUT':
        return jsonify(UsersDAO().update_user(user, request.json))

    if request.method == 'DELETE':
        UsersDAO().delete_user(user)
        return f"Запись под id {user_id} была удалена"
