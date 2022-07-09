import json

from classes.models import Offer
from config import OFFERS_DATA
from utils import db


class OffersDAO:
    """
    Класс для работы с базой данных исполнителей
    """

    def __init__(self, path=OFFERS_DATA):
        self.path = path

    def create_offers(self):
        """
        Создание базы данных исполнителей взятых из файла JSON
        """

        with open(self.path, encoding='UTF-8') as f:
            data = json.load(f)
            offers = [Offer(
                id=d['id'],
                order_id=d['order_id'],
                executor_id=d['executor_id']
            ) for d in data]
            db.session.add_all(offers)
            db.session.commit()

    def add_new(self, offer):
        """
        Добавление нового исполнителя
        """
        new_offer = Offer(
            order_id=offer.get('order_id'),
            executor_id=offer.get('executor_id')
        )
        db.session.add(new_offer)
        db.session.commit()
        return Offer.make_dict(new_offer)

    def update_offer(self, offer, update_offer):
        """
        Обновление данных исполнителя
        """
        offer.order_id = update_offer.get('order_id')
        offer.executor_id = update_offer.get('executor_id')
        db.session.add(offer)
        db.session.commit()
        return Offer.make_dict(offer)

    def delete_offer(self, offer):
        """
        Удаление данных исполнителя
        """
        db.session.delete(offer)
        db.session.commit()
