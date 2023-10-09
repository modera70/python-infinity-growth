class DriverManager:
    """Responsible for handling the WebDriver instance."""
    def __init__(self, driver_initializer):
        self._driver_initializer = driver_initializer
        self._driver = self.init_driver()

    def init_driver(self):
        return self._driver_initializer.initialize()

    @property
    def driver(self):
        """
        Return an instance of the WebDriver.
        :return:  WebDriver instance
        """
        return self._driver

    def quit_driver(self):
        """
        Dispose the instance of the WebDriver.
        :return: None
        """
        self._driver.quit()
