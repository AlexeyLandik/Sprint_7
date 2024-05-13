import pytest
from helpers_files.helpers import Courier


@pytest.fixture()
def order_data():
    order_data = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha"
    }
    return order_data


@pytest.fixture(scope='function')
def courier():
    courier = Courier()
    courier_data = courier.courier_datas_creation(10)
    return courier_data
