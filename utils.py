from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # создаем экземпляр класса SQLAlchemy(для использования во всех файлах проекта


def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False  # отключаем кодировку api для корректной работы json данных
    app.config['JSON_SORT_KEYS'] = False  # отключаем сортировку ключей json
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # подключение к базе данных в оперативной памяти
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    app.app_context().push()
    return app


class NotFoundById(Exception):  # ошибка для отсутствующих ID
    pass
