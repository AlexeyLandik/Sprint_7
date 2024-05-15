import requests
import random
import string
from data import Data
import allure


class Courier:

    @staticmethod
    @allure.step('Генерация случайной строки')
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    @allure.step('Получение случайных данных для создания курьера')
    def courier_datas_creation(length):
        login = Courier.generate_random_string(length)
        password = Courier.generate_random_string(length)
        first_name = Courier.generate_random_string(length)
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return payload

    @allure.step('Регистрация нового курьера и возврат его данных')
    def register_new_courier_and_return_login_password_first_name(self):
        login_pass = []
        payload = self.courier_datas_creation(10)
        response = requests.post(Data.CREATE_OR_DELETE_COURIER, data=payload)
        if response.status_code == 201:
            login_pass.append(payload['login'])
            login_pass.append(payload['password'])
            login_pass.append(payload['firstName'])
        return login_pass

    @allure.step('Регистрация курьера и возврат ответа сервера')
    def register_courier(self, user_data: dict):
        response = requests.post(Data.CREATE_OR_DELETE_COURIER, data=user_data)
        return response.json()

    @allure.step('Удаление курьера')
    def delete_courier(self, id_courier=3):
        response = requests.delete(Data.CREATE_OR_DELETE_COURIER + id_courier)
        return response.json()


class Order:

    @staticmethod
    @allure.step('Создание заказа')
    def create_order(order_data):
        response = requests.post(Data.CREATE_ORDER, data=order_data)
        return response

    @staticmethod
    @allure.step('Получение списка заказов')
    def get_order_list():
        response = requests.get(Data.CREATE_ORDER)
        return response
