from flask import Blueprint, request, jsonify

from app.offers.dao.offers_dao import OffersDAO
from classes.models import Offer
from utils import NotFoundById

offers_blueprint = Blueprint('offers_blueprint', __name__)


@offers_blueprint.route('/', methods=['GET', 'POST'])
def page_offers():
    """ Вьюшка:
    GET = все данные исполнителей
    POST = добавление данных исполнителя из JSON
    """

    if request.method == 'GET':
        offers = []
        for offer in Offer.query.all():
            offers.append(Offer.make_dict(offer))
        return jsonify(offers)

    if request.method == 'POST':
        data = request.json
        new_offer = OffersDAO().add_new(data)
        return jsonify(new_offer)


@offers_blueprint.route('/<int:offer_id>/', methods=['GET', 'PUT', 'DELETE'])
def page_update_users(offer_id):
    """ Вьюшка:
    GET = данные исполнителя по ID
    PUT = обновление данных исполнителя из полученного JSON
    DELETE = удаление данных исполнителя по ID
    """

    offer = Offer.query.get(offer_id)  # ищем исполнителя

    if offer is None:  # ошибка при отсутствии записи по ID

        raise NotFoundById
    if request.method == 'GET':
        return jsonify(Offer.make_dict(offer))

    if request.method == 'PUT':
        return jsonify(OffersDAO().update_offer(offer, request.json))

    if request.method == 'DELETE':
        OffersDAO().delete_offer(offer)
        return f"Запись под id {offer_id} была удалена"
