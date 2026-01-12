import allure
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators
from data import Urls
from locators.order_feed_page_locators import OrderPageLocators

class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ProfilePageLocators()
    
    @allure.step("Клик по кнопке 'История заказов'")
    def click_order_history_button(self):
        self.click_to_element(self.locators.ORDER_HISTORY_BUTTON)
        WebDriverWait(self.driver, 10).until(lambda d: d.current_url == Urls.ORDER_HISTORY_URL)
    
    @allure.step("Клик по кнопке 'Выход'")
    def click_logout_button(self):
        self.click_to_element(self.locators.LOGOUT_BUTTON)
        WebDriverWait(self.driver, 10).until(lambda d: d.current_url == Urls.LOGIN_URL)
    
    @allure.step("Клик по кнопке профиля")
    def click_profile_button(self):
        self.click_to_element(self.locators.PROFILE_BUTTON)
    
    @allure.step("Проверка что находимся на странице профиля")
    def is_profile_page(self):
        current_url = self.get_current_url()
        return current_url == Urls.PROFILE_URL
    
    @allure.step("Проверка что находимся на странице истории заказов")
    def is_order_history_page(self):
        return self.get_current_url() == Urls.ORDER_HISTORY_URL
    
    @allure.step("Проверка выхода из аккаунта")
    def is_logged_out(self):
        current_url = self.get_current_url()
        return current_url == Urls.LOGIN_URL
    
    @allure.step("Получаем элемент заказа из истории")
    def get_order_item_from_history(self):
        return self.get_random_element_in_multiple_elements(self.locators.ORDER_ITEM_IN_HISTORY)
    
    @allure.step("Получаем номер заказа из истории")
    def get_order_number_from_history(self):
        return self.get_random_element_in_multiple_elements(self.locators.ORDER_ITEM_NUMBER_IN_HISTORY).text.strip()
