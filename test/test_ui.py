from test.test_base_ui import TestBaseUi


class TestUi(TestBaseUi):

    def test_success_login_correct_user_and_password(self, login_page, home_page):
        login_page.open("https://www.saucedemo.com/")  # Arrange
        login_page.login("standard_user", "secret_sauce")
        assert home_page.is_page_loaded()

    def test_failed_login_incorrect_password(self, login_page):
        login_page.open("https://www.saucedemo.com/")  # Arrange
        login_page.login("standard_user", "incorrect_password")  # Act
        assert login_page.is_error_message_present()  # Assert

    def test_add_product_to_car(self, login_page, home_page, car_page):
        login_page.open("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")
        assert home_page.is_page_loaded()
        home_page.add_item_to_car()
        home_page.go_to_shopping_car_page()
        assert len(car_page.get_card_items()) > 0

    def test_fail_add_product_to_car(self, login_page, home_page, car_page):
        login_page.open("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")
        assert home_page.is_page_loaded()
        home_page.add_item_to_car()
        home_page.go_to_shopping_car_page()
        assert len(car_page.get_card_items()) == 0
