from selenium import webdriver


class RemoteWebdriverInitializer:

    def __init__(self, driver_configuration):
        self.driver_configuration = driver_configuration

    def initialize(self):
        desired_cap = self.driver_configuration.get_capabilities()
        driver = webdriver.Remote(
            command_executor=self.driver_configuration.get_hub_url(),
            desired_capabilities=desired_cap)
        driver.maximize_window()
        driver.implicitly_wait(self.driver_configuration.get_timeout())
        return driver
