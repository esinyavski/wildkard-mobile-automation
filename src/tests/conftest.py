import os
import sys
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))

from src.wrappers.driver import Driver
from src.utils.config_parser import parse_config
from src.utils.data_generator import DataGenerator
from src.app.features.login import Login
from src.app.features.landing import Landing


@pytest.fixture(scope='session', autouse=True)
def base_config():
    return parse_config()


@pytest.fixture()
def driver(base_config):
    Driver.init_driver(config=base_config)
    yield Driver.driver
    Driver.driver.quit()


@pytest.fixture(scope='session')
def dummy():
    return DataGenerator


@pytest.fixture
def login():
    return Login()


@pytest.fixture
def landing():
    return Landing()


@pytest.fixture
def organizing(landing, dummy):
    landing.click__league_menu()
    return landing.select_league_from_menu(name=dummy.LEAGUE_NAME)
