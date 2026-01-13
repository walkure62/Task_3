import allure
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderPageLocators
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
        self.click_to_element_with_script(close_button)
        self.wait_for_modal_close(self.locators.ORDER_FEED_MODAL)
    
    @allure.step("Получаем счетчик заказов за все время")
    def get_order_counter_all_time(self):
        self.is_element_present(self.locators.ORDER_COUNTER_ALL_TIME, timeout=5)
        order_counter_text = self.get_text_from_element(self.locators.ORDER_COUNTER_ALL_TIME)
        order_counter_num = int(order_counter_text)
        return order_counter_num
    
    @allure.step("Получаем счетчик заказов за сегодня")
    def get_order_counter_today(self):
        self.is_element_present(self.locators.ORDER_COUNTER_TODAY, timeout=5)
        order_counter_text = self.get_text_from_element(self.locators.ORDER_COUNTER_TODAY)
        order_counter_num = int(order_counter_text)
        return order_counter_num
    
    @allure.step("Получаем список заказов в работе")
    def get_orders_in_progress(self):
        self.is_element_present(self.locators.ORDER_LIST_IN_PROGRESS)
        order_numbers = self.wait_and_find_elements(self.locators.ORDER_NUMBER_IN_PROGRESS)
        order_numbers_list = []
        for order in order_numbers:
            order_numbers_list.append(order.text.strip())
        return order_numbers_list
    
    @allure.step("Проверка что находимся на странице ленты заказов")
    def is_order_feed_page(self):
        return self.get_current_url() == Urls.LIST_OF_ORDERS_URL
    
    @allure.step("Ожидание появления номера заказа в ленте заказов")
    def wait_for_order_in_feed(self, order_number, timeout=15):
        from selenium.webdriver.support.ui import WebDriverWait
        order_items = self.get_order_numbers_in_feed()
        WebDriverWait(self.driver, timeout).until(lambda d: order_number in order_items)
    
    @allure.step("Получаем список номеров заказов в ленте")
    def get_order_numbers_in_feed(self):
        order_items = self.wait_and_find_elements(self.locators.ORDER_ITEM_NUMBER_IN_FEED, required=False)
        return [item.text.strip() for item in order_items]
    