import allure
from locators import order_feed_page_locators
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
from data import Urls

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators()
    
    @allure.step("Клик по элементу заказа в ленте")
    def click_order_item(self):
        order_item = self.get_random_element_in_multiple_elements(self.locators.ORDER_ITEM_IN_FEED)
        self.scroll_to_element(order_item)
        order_item.click()
    
    @allure.step("Проверка открытия модального окна с информацией о заказе")
    def is_order_modal_open(self):
        return self.is_element_visible(OrderPageLocators.ORDER_FEED_MODAL, timeout=5)
    
    @allure.step("Закрытие модального окна с информацией о заказе")
    def close_order_modal(self):
        close_button = self.wait_and_find_element(OrderPageLocators.ORDER_FEED_MODAL_CLOSE_BUTTON, timeout=3)
        self.driver.execute_script("arguments[0].click();", close_button)
    
    @allure.step("Получаем счетчик заказов за все время")
    def get_order_counter_all_time(self):
        self.is_element_present(self.locators.ORDER_COUNTER_ALL_TIME, timeout=5)
        return self.get_text_from_element(self.locators.ORDER_COUNTER_ALL_TIME)
    
    @allure.step("Получаем счетчик заказов за сегодня")
    def get_order_counter_today(self):
        self.is_element_present(self.locators.ORDER_COUNTER_TODAY, timeout=5)
        return self.get_text_from_element(self.locators.ORDER_COUNTER_TODAY)
    
    @allure.step("Получаем список заказов в работе")
    def get_orders_in_progress(self):
        if self.is_element_present(self.locators.ORDER_LIST_IN_PROGRESS):
            order_numbers = self.wait_and_find_elements(self.locators.ORDER_NUMBER_IN_PROGRESS)
            order_numbers_list = []
            for order in order_numbers:
                if int(order.text.strip()):
                    order_numbers_list.append(order.text.strip())
            return order_numbers_list
        return []
    
    @allure.step("Проверка что находимся на странице ленты заказов")
    def is_order_feed_page(self):
        return self.get_current_url() == Urls.LIST_OF_ORDERS_URL
    