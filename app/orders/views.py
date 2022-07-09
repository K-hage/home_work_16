from flask import Blueprint, request, jsonify

from app.orders.dao.orders_dao import OrdersDAO
from classes.models import Order
from utils import NotFoundById

orders_blueprint = Blueprint('orders_blueprint', __name__)


@orders_blueprint.route('/', methods=['GET', 'POST'])
def page_orders():
    """ Вьюшка:
    GET = все данные заказчиков
    POST = добавление данных заказчика из JSON
    """

    if request.method == 'GET':
        orders = []
        for order in Order.query.all():
            orders.append(Order.make_dict(order))
        return jsonify(orders)

    if request.method == 'POST':
        data = request.json
        new_order = OrdersDAO().add_new(data)
        return jsonify(new_order)


@orders_blueprint.route('/<int:order_id>/', methods=['GET', 'PUT', 'DELETE'])
def page_update_users(order_id):
    """ Вьюшка:
    GET = данные заказчика по ID
    PUT = обновление данных заказчика из полученного JSON
    DELETE = удаление данных заказчика по ID
    """

    order = Order.query.get(order_id)  # ищем заказчика

    if order is None:  # ошибка при отсутствии записи по ID
        raise NotFoundById
    if request.method == 'GET':
        return jsonify(Order.make_dict(order))

    if request.method == 'PUT':
        return jsonify(OrdersDAO().update_order(order, request.json))

    if request.method == 'DELETE':
        OrdersDAO().delete_order(order)
        return f"Запись под id {order_id} была удалена"
