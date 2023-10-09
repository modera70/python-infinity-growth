import time

from selenium.webdriver.remote.webdriver import WebDriver
from seleniumpagefactory import PageFactory


class BasePage(PageFactory):

    def __init__(self, driver):
        self.driver = driver

    @property
    def title(self):
        return self.driver.title

    def open(self, url):
        self.driver.get(url)

    def scroll_to_element(self, selector, value):
        element = self.find_element(selector, value)
        self.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)


WebDriver.scroll_to_element = BasePage.scroll_to_element
