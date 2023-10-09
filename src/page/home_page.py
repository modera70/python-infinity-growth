import time

from selenium.webdriver.common.by import By

from src.page.basepage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    locators = {
        "app_logo_container": ('CSS', "div.app_logo"),
        "shopping_car_container": ('ID', "shopping_cart_container"),
    }

    def is_page_loaded(self):
        return "Swag Labs" in self.app_logo_container.get_text()

    def add_item_to_car(self):
        add_to_car_buttons = self.driver.find_elements(By.CSS_SELECTOR, "button.btn_inventory")
        add_to_car_buttons[0].click()

    def go_to_shopping_car_page(self):
        self.shopping_car_container.click_button()

