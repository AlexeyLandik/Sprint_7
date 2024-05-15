# Sprint_7
# Финальный проект 7 спринта
В проекте содержатся тесты сервиса «Яндекс.Самокат».
## Описание файлов
- tests/test_courier.py - файл с тестами Курьера
- tests/test_orders.py - файл с тестами Заказов
- tests/conftest.py - файл с фикстурами
- .gitignore - перечень игнорируемых файлов и директорий
- data.py - константы 
- README.md - описание проекта
- requirements.txt - зависимости, для разворачивания проекта
## Инструкция для запуска проекта
1. Клонируйте репозиторий в рабочую папку
2. Разверните виртуальное окружение `python -m venv .venv`
3. Активируйте виртуальное окружение `.\.venv\Scripts\activate`
4. Установить зависимости `pip install -r requirements.txt`
5. Запустить автотесты `pytest tests --alluredir=allure_results` 
6. Запустить формирование отчета в allure `allure serve allure_results`
