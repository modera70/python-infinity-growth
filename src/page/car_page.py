import time

from selenium.webdriver.common.by import By

from src.page.basepage import BasePage


class CarPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_card_items(self,):
        return self.driver.find_elements(By.CSS_SELECTOR, "div.cart_item")

