import uuid

import allure
import pytest

from src.common.driver_type import Driver
from src.config.driver_config import JsonDiverConfiguration
from src.config.driver_initializer import RemoteWebdriverInitializer
from src.config.driver_manager import DriverManager
from src.page.login_page import LoginPage
from src.page.home_page import HomePage
from src.page.car_page import CarPage


class TestBaseUi:

    @pytest.fixture(params=Driver)
    def driver_configuration(self, request):
        return JsonDiverConfiguration(request.param)

    @pytest.fixture()
    def driver_initializer(self, driver_configuration):
        return RemoteWebdriverInitializer(driver_configuration)

    @pytest.fixture()
    def driver_manager(self, driver_initializer, driver_configuration):
        driver_manager = DriverManager(driver_initializer)
        try:
            yield driver_manager

            screenshot = f"{driver_configuration.driver_type.name}_{uuid.uuid1()}.png"
            driver_manager.driver.save_screenshot(screenshot)
            allure.attach.file(screenshot, attachment_type=allure.attachment_type.PNG)
        finally:
            driver_manager.quit_driver()

    @pytest.fixture()
    def login_page(self, driver_manager):
        return LoginPage(driver_manager.driver)

    @pytest.fixture()
    def home_page(self, driver_manager):
        return HomePage(driver_manager.driver)

    @pytest.fixture()
    def car_page(self, driver_manager):
        return CarPage(driver_manager.driver)
