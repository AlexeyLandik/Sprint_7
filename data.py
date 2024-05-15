class Data:

    BASE_URL = 'https://qa-scooter.praktikum-services.ru'  # Базовый URL

    CREATE_OR_DELETE_COURIER = BASE_URL + '/api/v1/courier/'  # Ручка для создания или удаления курьера
    CREATE_COURIER = BASE_URL + '/api/v1/courier'  # Ручка для создания курьера
    LOGIN_COURIER = BASE_URL + '/api/v1/courier/login'  # Ручка для авторизации курьера
    DELETE_COURIER = BASE_URL + '/api/v1/courier/'  # Ручка для удаления курьера

    CREATE_ORDER = BASE_URL + '/api/v1/orders'  # Ручка для создания и получения списка заказов

    # Данные для заказа
    ORDER_DATA = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha"
        }
