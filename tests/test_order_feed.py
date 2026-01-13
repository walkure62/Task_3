import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.order_feed_page import OrderPage

class TestOrderFeed:
    
    @allure.description("Проверка открытия модального окна с деталями заказа при клике")
    def test_order_modal_opens_on_click(self, driver, login):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        main_page.click_order_button()
        order_page.click_order_item()
        
        assert order_page.is_order_modal_open(), "Всплывающее окно с деталями заказа не открылось"
    
    @allure.description("Проверка отображения заказов пользователя в ленте заказов")
    def test_user_orders_displayed_in_feed(self, driver, login):
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        order_page = OrderPage(driver)

        ingredient = main_page.get_random_ingredient()
    
        main_page.create_order(ingredient)
        main_page.click_profile_button()
        profile_page.click_order_history_button()
        
        order_item_history_number = profile_page.get_order_number_from_history()
        
        main_page.click_order_button()
        order_page.wait_for_order_in_feed(order_item_history_number)
        
        order_numbers_feed = order_page.get_order_numbers_in_feed()
        
        assert order_item_history_number in order_numbers_feed, f"Заказы пользователя из раздела 'История заказов' не отображаются на странице 'Лента заказов'. Номер заказа: {order_item_history_number}, Найденные номера: {order_numbers_feed}"
    
    @allure.description("Проверка увеличения счетчика 'Выполнено за всё время' при создании нового заказа")
    def test_all_time_counter_increases_on_new_order(self, driver, login):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        main_page.click_order_button()
        
        initial_counter = order_page.get_order_counter_all_time()
    
        main_page.click_constructor_button()
        
        ingredient = main_page.get_random_ingredient()
        
        main_page.create_order(ingredient)
        main_page.click_order_button()
        
        new_counter = order_page.get_order_counter_all_time() # Новые данные отображаются на странице ленты заказов с большой задержкой, помог time.sleep(40). Но не считаю правильным использовать большую задержку в тесте, считаю это багом.
        
        assert new_counter > initial_counter, f'Счётчик "Выполнено за всё время" не увеличился при создании нового заказа. Было: {initial_counter}, стало: {new_counter}'
    
    @allure.description("Проверка увеличения счетчика 'Выполнено за сегодня' при создании нового заказа")
    def test_today_counter_increases_on_new_order(self, driver, login):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        main_page.click_order_button()
        
        initial_counter = order_page.get_order_counter_today()
        
        main_page.click_constructor_button()
        
        ingredient = main_page.get_random_ingredient()
        
        main_page.create_order(ingredient)
        main_page.click_order_button()
        
        new_counter = order_page.get_order_counter_today()
        
        assert new_counter > initial_counter, f'Счётчик "Выполнено за сегодня" не увеличился при создании нового заказа. Было: {initial_counter}, стало: {new_counter}'
    
    @allure.description("Проверка появления номера заказа в разделе 'В работе'")
    def test_order_number_appears_in_progress_section(self, driver, login):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        ingredient = main_page.get_random_ingredient()
        main_page.add_ingredient_to_order(ingredient)
        main_page.click_create_order_button()
        
        order_number = main_page.get_order_number()
        
        main_page.close_order_modal()
        main_page.click_order_button()
        
        orders_in_progress = order_page.get_orders_in_progress() # Новые данные отображаются на странице ленты заказов с большой задержкой, помог time.sleep(40). Но не считаю правильным использовать большую задержку в тесте, считаю это багом.
        
        assert order_number in orders_in_progress, f'Номер заказа {order_number} не появился в разделе "В работе". Текущие заказы: {orders_in_progress}'
