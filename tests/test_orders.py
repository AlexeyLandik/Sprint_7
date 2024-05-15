from helpers_files.helpers import Order
import json
import pytest
from data import Data
import allure


@allure.story('Тестирование Заказов')
class TestCreateOrders:

    @allure.title('Тест. Создание заказа. Указан один цвет, два цвета, не указан цвет. Код 201, запрос возвращает track'
                  ' номер')
    @pytest.mark.parametrize(
        'color_value',
        [
            ["BLACK"],
            ["GRAY"],
            ["BLACK", "GRAY"],
            []
        ]
    )
    def test_create_order_with_color(self, color_value):
        order = Order()
        Data.ORDER_DATA["color"] = color_value
        response = order.create_order(json.dumps(Data.ORDER_DATA))
        assert response.status_code == 201 and 'track' in response.text

    @allure.title('Тест. Список заказов. Получение списка заказов. Приходит список заказов')
    def test_get_order_list(self):
        order = Order
        response = order.get_order_list()
        assert "orders" in response.text
