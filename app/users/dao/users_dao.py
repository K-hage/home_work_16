import json

from classes.models import User
from config import USERS_DATA
from utils import db


class UsersDAO:
    """
    Класс для работы с базами данных заказчиков
    """

    def __init__(self, path=USERS_DATA):
        self.path = path

    def create_users(self):
        """
        Заполнение базы данных заказчиков из JSON файла
        """

        with open(self.path, encoding='UTF-8') as f:
            data = json.load(f)
            users = [User(
                id=d['id'],
                first_name=d['first_name'],
                last_name=d['last_name'],
                age=d['age'],
                email=d['email'],
                role=d['role'],
                phone=d['phone']
            ) for d in data]
            db.session.add_all(users)
            db.session.commit()

    def add_new(self, user):
        """
        Добавление нового заказчика
        """

        new_user = User(
            first_name=user.get('first_name'),
            last_name=user.get('last_name'),
            age=user.get('age'),
            email=user.get('email'),
            role=user.get('role'),
            phone=user.get('phone'))
        db.session.add(new_user)
        db.session.commit()
        return User.make_dict(new_user)

    def update_user(self, user, update_user):
        """
        Обновление данных заказчика
        """

        user.first_name = update_user.get('first_name')
        user.last_name = update_user.get('last_name')
        user.age = update_user.get('age')
        user.email = update_user.get('email')
        user.role = update_user.get('role')
        user.phone = update_user.get('phone')
        db.session.add(user)
        db.session.commit()
        return User.make_dict(user)

    def delete_user(self, user):
        """
        Удаление данных заказчика
        """

        db.session.delete(user)
        db.session.commit()
