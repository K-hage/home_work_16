from os import path

parent_dir = path.dirname(path.abspath(__file__))
USERS_DATA = path.join(parent_dir, 'data', 'users.json')  # путь к данным пользователей
OFFERS_DATA = path.join(parent_dir, 'data', 'offers.json')  # путь к данным исполнителей
ORDERS_DATA = path.join(parent_dir, 'data', 'orders.json')  # путь к данным заказчиков
