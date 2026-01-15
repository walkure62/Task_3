import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from data import Urls

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = LoginPageLocators()
    
    @allure.step("Вводим email")
    def enter_email(self, email):
        self.send_keys_to_element(self.locators.EMAIL_INPUT, email)
    
    @allure.step("Вводим пароль")
    def enter_password(self, password):
        self.send_keys_to_element(self.locators.PASSWORD_INPUT, password)
    
    @allure.step("Клик по кнопке 'Войти'")
    def click_login_button(self):
        self.click_to_element(self.locators.LOGIN_BUTTON)
    
    @allure.step("Клик по кнопке 'Восстановить пароль'")
    def click_restore_password_button(self):
        self.click_to_element(self.locators.RESTORE_PASSWORD_BUTTON)
        self.wait_for_url_change(Urls.FORGOT_PASSWORD_URL)
    
    @allure.step("Авторизация пользователя")
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
    
    @allure.step("Проверка что находимся на странице входа")
    def is_login_page(self):
        return self.get_current_url() == Urls.LOGIN_URL
