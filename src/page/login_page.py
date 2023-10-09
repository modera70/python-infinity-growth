from src.page.basepage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # define locators dictionary where key name will become WebElement using PageFactory
    locators = {
        "username_text_box": ('ID', 'user-name'),
        "password_text_box": ('ID', 'password'),
        "login_button": ('ID', 'login-button'),
        "error_message_container": ('CSS', 'div.error-message-container > h3')
    }

    def login(self, username, password):
        self.username_text_box.set_text(username)
        self.password_text_box.set_text(password)
        self.login_button.click_button()

    def is_error_message_present(self):
        return "Username and password do not match any user in this service" in self.error_message_container.get_text()


