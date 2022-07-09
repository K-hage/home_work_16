import json

from classes.models import Order
from config import ORDERS_DATA
from utils import db


class OrdersDAO:
    """
    Класс для работы с базами данных заказчиков
    """

    def __init__(self, path=ORDERS_DATA):
        self.path = path

    def create_orders(self):
        """
        Заполнение базы данных заказчиков из JSON файла
        """

        with open(self.path, encoding='UTF-8') as f:
            data = json.load(f)
            orders = [Order(
                id=d['id'],
                name=d['name'],
                description=d['description'],
                start_date=d['start_date'],
                end_date=d['end_date'],
                address=d['address'],
                price=d['price'],
                customer_id=d['customer_id'],
                executor_id=d['executor_id']
            ) for d in data]
            db.session.add_all(orders)
            db.session.commit()

    def add_new(self, order):
        """
        Добавление нового заказчика
        """

        new_order = Order(
            name=order.get('name'),
            description=order.get('description'),
            start_date=order.get('start_date'),
            end_date=order.get('end_date'),
            address=order.get('address'),
            price=order.get('price'),
            customer_id=order.get('customer_id'),
            executor_id=order.get('executor_id')
        )
        db.session.add(new_order)
        db.session.commit()
        return Order.make_dict(new_order)

    def update_order(self, order, update_order):
        """
        Обновление данных заказчика
        """

        order.name = update_order.get('name')
        order.description = update_order.get('description')
        order.start_date = update_order.get('start_date')
        order.end_date = update_order.get('end_date')
        order.address = update_order.get('address')
        order.price = update_order.get('price')
        order.customer_id = update_order.get('customer_id')
        order.executor_id = update_order.get('executor_id')
        db.session.add(order)
        db.session.commit()
        return Order.make_dict(order)

    def delete_order(self, order):
        """
        Удаление данных заказчика
        """

        db.session.delete(order)
        db.session.commit()


