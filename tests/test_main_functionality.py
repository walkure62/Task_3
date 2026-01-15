import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderPage

class TestMainFunctionality:
    
    @allure.description("Проверка навигации на страницу конструктора")
    def test_navigate_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_constructor_button()
        
        assert main_page.is_constructor_section_visible(), "Не удалось перейти по клику на 'Конструктор'"
    
    @allure.description("Проверка навигации на страницу ленты заказов")
    def test_navigate_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_button()
        
        order_page = OrderPage(driver)
        assert order_page.is_order_feed_page(), "Не удалось перейти по клику на 'Лента заказов'"
    
    @allure.description("Проверка открытия модального окна с деталями ингредиента при клике")
    def test_ingredient_modal_opens_on_click(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        main_page.wait_for_page_load()
        
        assert main_page.is_ingredient_modal_open(), "Всплывающее окно с деталями ингредиента не появилось"
    
    @allure.description("Проверка закрытия модального окна ингредиента при клике на крестик")
    def test_ingredient_modal_closes_on_x_click(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        main_page.close_ingredient_modal()
        assert not main_page.is_ingredient_modal_open(), "Всплывающее окно не закрылось при клике на крестик"
    
    @allure.description("Проверка увеличения счетчика ингредиента при добавлении в заказ")
    def test_ingredient_counter_increases_on_add(self, driver):
        main_page = MainPage(driver)
        
        ingredient = main_page.get_random_ingredient()
        initial_counter = main_page.get_ingredient_counter(ingredient)
        main_page.add_ingredient_to_order(ingredient)
        
        new_counter = main_page.get_ingredient_counter(ingredient)
        
        assert new_counter > initial_counter, f'Счетчик ингредиента не увеличился при добавлении в заказ. Было: {initial_counter}, стало: {new_counter}'
    
    
    @allure.description("Проверка возможности создания заказа залогиненным пользователем")
    def test_logged_in_user_can_create_order(self, driver, login):
        main_page = MainPage(driver)
        
        ingredient = main_page.get_random_ingredient()
        main_page.add_ingredient_to_order(ingredient)
        main_page.click_create_order_button()
        
        assert main_page.is_order_modal_open(), "Залогиненный пользователь не может оформить заказ"
