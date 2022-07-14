import pytest
import logging
from selenium import webdriver

from tests import test_number_one
from tests import test_number_two


logging.basicConfig(
    level=logging.DEBUG,
    filename = "mylog.log",
    format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
    )

@pytest.fixture(scope="session")
def start_tests():
    test_number_one()
    test_number_two()

