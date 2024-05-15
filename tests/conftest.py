import pytest
from helpers_files.helpers import Courier


@pytest.fixture(scope='function')
def courier():
    courier = Courier()
    courier_data = courier.courier_datas_creation(10)
    return courier_data
