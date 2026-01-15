import allure
from pages.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from data import Urls

class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ForgotPasswordPageLocators()
    
    @allure.step("Вводим email")
    def enter_email(self, email):
        self.send_keys_to_element(self.locators.EMAIL_INPUT, email)
    
    @allure.step("Вводим пароль")
    def enter_password(self, password):
        self.send_keys_to_element(self.locators.PASSWORD_INPUT, password)
    
    @allure.step("Клик по кнопке 'Восстановить'")
    def click_restore_button(self):
        self.wait_for_element_to_be_clickable(self.locators.RESTORE_BUTTON, timeout=5)
        self.click_to_element(self.locators.RESTORE_BUTTON)
        self.wait_for_url_change(Urls.RESET_PASSWORD_URL)
    
    @allure.step("Клик по кнопке показать/скрыть пароль")
    def click_show_password_button(self):
        self.wait_for_element_to_be_clickable(self.locators.SHOW_PASSWORD_BUTTON, timeout=5)
        self.click_to_element(self.locators.SHOW_PASSWORD_BUTTON)
    
    @allure.step("Проверка активности поля ввода пароля")
    def is_password_input_active(self):
        return self.is_element_present(self.locators.PASSWORD_INPUT_ACTIVE, timeout=3)
    
    @allure.step("Проверка подсветки поля ввода пароля")
    def is_password_field_highlighted(self):
        password_input = self.wait_and_find_element(self.locators.PASSWORD_INPUT_ACTIVE, timeout=3)
        class_attr = password_input.get_attribute("class")
        return "input_status_active" in class_attr or self.is_element_present(self.locators.PASSWORD_INPUT_ACTIVE, timeout=1)
    
    @allure.step("Проверка что находимся на странице восстановления пароля")
    def is_forgot_password_page(self):
        return self.get_current_url() == Urls.FORGOT_PASSWORD_URL
    
    @allure.step("Проверка что находимся на странице сброса пароля")
    def is_reset_password_page(self):
        return self.get_current_url() == Urls.RESET_PASSWORD_URL 
    
