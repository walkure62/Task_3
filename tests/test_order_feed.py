import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.order_feed_page import OrderPage
from data import Urls

class TestOrderFeed:
    
    @allure.description("Проверка открытия модального окна с деталями заказа при клике")
    def test_order_modal_opens_on_click(self, driver, login):
        order_page = OrderPage(driver)
        driver.get(Urls.LIST_OF_ORDERS_URL)
        
        order_page.click_order_item()
        assert order_page.is_order_modal_open(), "Всплывающее окно с деталями заказа не открылось"
    
    @allure.description("Проверка отображения заказов пользователя в ленте заказов")
    def test_user_orders_displayed_in_feed(self, driver, login):
        main_page = MainPage(driver)
        driver.get(Urls.BASE_URL)
        main_page.create_order()
        
        profile_page = ProfilePage(driver)
        main_page.click_profile_button()
        profile_page.click_order_history_button()
        
        order_item_history_number = profile_page.get_order_number_from_history()
        
        driver.get(Urls.LIST_OF_ORDERS_URL)
        order_page = OrderPage(driver)
        
        WebDriverWait(driver, 15).until(
            lambda d: order_item_history_number in [
                item.text.strip() 
                for item in order_page.wait_and_find_elements(order_page.locators.ORDER_ITEM_NUMBER_IN_FEED, required=False)
            ]
        )
        
        order_items_number_in_feed = order_page.wait_and_find_elements(order_page.locators.ORDER_ITEM_NUMBER_IN_FEED, required=False)
        order_numbers_feed = [item.text.strip() for item in order_items_number_in_feed]
        
        assert order_item_history_number in order_numbers_feed, f"Заказы пользователя из раздела 'История заказов' не отображаются на странице 'Лента заказов'. Номер заказа: {order_item_history_number}, Найденные номера: {order_numbers_feed}"
    
    @allure.description("Проверка увеличения счетчика 'Выполнено за всё время' при создании нового заказа")
    def test_all_time_counter_increases_on_new_order(self, driver, login):
        order_page = OrderPage(driver)
        driver.get(Urls.LIST_OF_ORDERS_URL)
        
        initial_counter_text = order_page.get_order_counter_all_time()
        initial_counter = int(initial_counter_text)
        
        main_page = MainPage(driver)
        driver.get(Urls.BASE_URL)
        
        main_page.add_ingredient_to_order()
        main_page.click_create_order_button()
        main_page.close_order_modal()
        
        driver.get(Urls.LIST_OF_ORDERS_URL)
        
        new_counter_text = order_page.get_order_counter_all_time() # Новые данные отображаются на странице ленты заказов с большой задержкой, помог time.sleep(40). Но не считаю правильным использовать большую задержку в тесте, считаю это багом.
        new_counter = int(new_counter_text)
        
        assert new_counter > initial_counter, f'Счётчик "Выполнено за всё время" не увеличился при создании нового заказа. Было: {initial_counter}, стало: {new_counter}'
    
    @allure.description("Проверка увеличения счетчика 'Выполнено за сегодня' при создании нового заказа")
    def test_today_counter_increases_on_new_order(self, driver, login):
        order_page = OrderPage(driver)
        driver.get(Urls.LIST_OF_ORDERS_URL)
        
        initial_counter_text = order_page.get_order_counter_today()
        initial_counter = int(initial_counter_text)
        
        main_page = MainPage(driver)
        driver.get(Urls.BASE_URL)
        
        main_page.add_ingredient_to_order()
        main_page.click_create_order_button()
        main_page.close_order_modal()
        
        driver.get(Urls.LIST_OF_ORDERS_URL)
        
        new_counter_text = order_page.get_order_counter_today()
        new_counter = int(new_counter_text)
        
        assert new_counter > initial_counter, f'Счётчик "Выполнено за сегодня" не увеличился при создании нового заказа. Было: {initial_counter}, стало: {new_counter}'
    
    @allure.description("Проверка появления номера заказа в разделе 'В работе'")
    def test_order_number_appears_in_progress_section(self, driver, login):
        main_page = MainPage(driver)
        driver.get(Urls.BASE_URL)
        
        main_page.add_ingredient_to_order()
        main_page.click_create_order_button()
        order_number = main_page.get_order_number()
        main_page.close_order_modal()
        
        order_page = OrderPage(driver)
        driver.get(Urls.LIST_OF_ORDERS_URL)
        
        orders_in_progress = order_page.get_orders_in_progress() # Новые данные отображаются на странице ленты заказов с большой задержкой, помог time.sleep(40). Но не считаю правильным использовать большую задержку в тесте, считаю это багом.
        
        assert order_number in orders_in_progress, f'Номер заказа {order_number} не появился в разделе "В работе". Текущие заказы: {orders_in_progress}'
