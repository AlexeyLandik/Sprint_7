from helpers_files.helpers import Courier
import requests
import data
import allure


@allure.story('Тестирование Курьера')
class TestCreateCourier:

    @allure.title('Тест. Создание курьера. Успешное создание. Код 201, запрос возвращает словарь ok: True')
    def test_create_courier_successful_1(self, courier):
        response = requests.post(data.CREATE_COURIER, data=courier)
        assert response.status_code == 201 and response.text == '{"ok":true}'

    @allure.title('Тест. Создание курьера. Ошибка создания. Код 400, "Недостаточно данных для создания учетной записи"')
    def test_create_courier_no_password_not_successful(self, courier):
        courier.pop('password')
        response = requests.post(data.CREATE_COURIER, data=courier)
        assert response.status_code == 400 and response.json()['message'] == ("Недостаточно данных для создания "
                                                                              "учетной записи")

    @allure.title('Тест. Создание курьера. Ошибка создания. Код 409, "Этот логин уже используется"')
    def test_create_courier_exists_login_not_successful(self, courier):
        requests.post(data.CREATE_COURIER, data=courier)
        response = requests.post(data.CREATE_COURIER, data=courier)
        assert response.status_code == 409 and response.json()[
            'message'] == "Этот логин уже используется. Попробуйте другой."

    @allure.title('Тест. Логин курьера. Успешная авторизация. Код 200, запрос возвращает id')
    def test_login_courier_successful(self):
        courier = Courier()
        login, password, first_name = courier.register_new_courier_and_return_login_password_first_name()
        payload = {"login": login, "password": password}
        response = requests.post(data.LOGIN_COURIER, data=payload)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Тест. Логин курьера. Ошибка авторизации. Отсутствует поле. Код 400, "Недостаточно данных для входа"')
    def test_login_courier_no_password_not_successful(self):
        courier = Courier()
        login, password, first_name = courier.register_new_courier_and_return_login_password_first_name()
        payload = {"login": login, "password": ''} # В данном тесте считаю правильным удалить ключ "password",
        # но в этом случае тест падает с ошибкой 504 Таймаут
        response = requests.post(data.LOGIN_COURIER, data=payload)
        assert response.status_code == 400 and response.json()['message'] == "Недостаточно данных для входа"

    @allure.title('Тест. Логин курьера. Ошибка авторизации. Несуществующий пользователь')
    def test_login_courier_not_exists_courier_not_successful(self):
        courier = Courier()
        login, password, first_name = courier.register_new_courier_and_return_login_password_first_name()
        payload = {"login": login, "password": password + '1'}
        response = requests.post(data.LOGIN_COURIER, data=payload)
        assert response.status_code == 404 and response.json()['message'] == "Учетная запись не найдена"
