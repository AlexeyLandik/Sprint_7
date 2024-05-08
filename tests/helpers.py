import requests
import random
import string
import data
import allure


class Courier:

    @staticmethod
    @allure.step('Генерация случайной строки')
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @allure.step('Получение случайных данных для создания курьера')
    def courier_datas_creation(self, length):
        login = self.generate_random_string(length)
        password = self.generate_random_string(length)
        first_name = self.generate_random_string(length)
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
        response = requests.post(data.CREATE_COURIER, data=payload)
        if response.status_code == 201:
            login_pass.append(payload['login'])
            login_pass.append(payload['password'])
            login_pass.append(payload['firstName'])
        return login_pass

    @allure.step('Регистрация курьера и возврат ответа сервера')
    def register_courier(self, user_data: dict):
        response = requests.post(data.CREATE_COURIER, data=user_data)
        print(response.text)
        return response.json()


class Order:

    def __init__(self, order_data):
        self.order_data = order_data

    @staticmethod
    @allure.step('Создание заказа')
    def create_order(order_data):
        response = requests.post(data.CREATE_ORDER, data=order_data)
        return response

    @staticmethod
    @allure.step('Получение списка заказов')
    def get_order_list():
        response = requests.get(data.CREATE_ORDER)
        return response
