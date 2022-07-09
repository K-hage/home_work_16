from app.errors.views import errors_blueprint
from app.offers.views import offers_blueprint
from app.orders.views import orders_blueprint
from app.users.dao.users_dao import UsersDAO
from app.orders.dao.orders_dao import OrdersDAO
from app.offers.dao.offers_dao import OffersDAO
from app.users.views import users_blueprint
from utils import db, create_app

app = create_app()  # создаем app и связь с бд через функцию

db.create_all()  # Создаем пустые таблицы

UsersDAO().create_users()  # Заполняем таблицу пользователей
OrdersDAO().create_orders()  # Заполняем таблицу заказчиков
OffersDAO().create_offers()  # Заполняем таблицу исполнителей

app.register_blueprint(users_blueprint, url_prefix='/users/')  # регистрируем блюпринт пользователей
app.register_blueprint(offers_blueprint, url_prefix='/offers/')  # регистрируем блюпринт исполнителей
app.register_blueprint(orders_blueprint, url_prefix='/orders/')  # регистрируем блюпринт заказчиков
app.register_blueprint(errors_blueprint)

if __name__ == "__main__":
    app.run(host="127.0.0.10", port=8080, debug=True)
