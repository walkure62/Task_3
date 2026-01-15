import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import Urls

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()
    
    @allure.step("Клик по кнопке 'Войти в аккаунт'")
    def click_login_button(self):
        self.click_to_element(self.locators.LOGIN_BUTTON)
        self.wait_for_url_change(Urls.LOGIN_URL)
    
    @allure.step("Клик по кнопке 'Конструктор'")
    def click_constructor_button(self):
        self.click_to_element(self.locators.CONSTRUCTOR_BUTTON)
    
    @allure.step("Клик по кнопке 'Лента Заказов'")
    def click_order_button(self):
        button = self.wait_for_element_to_be_clickable(self.locators.ORDER_BUTTON)
        self.click_to_element_with_script(button)
        self.wait_for_url_change(Urls.LIST_OF_ORDERS_URL)
    
    @allure.step("Клик по кнопке 'Личный Кабинет'")
    def click_profile_button(self):
        profile_button = self.wait_and_find_element(self.locators.PROFILE_BUTTON)
        self.click_to_element_with_script(profile_button)
        self.wait_for_url_change(Urls.PROFILE_URL)
    
    @allure.step("Получаем случайный ингредиент")
    def get_random_ingredient(self):
        ingredient = self.get_random_element_in_multiple_elements(self.locators.INGREDIENT_ITEM)
        return ingredient
    
    @allure.step("Клик по ингредиенту")
    def click_ingredient(self):
        ingredient = self.get_random_ingredient()
        self.scroll_to_element(ingredient)
        ingredient.click()
    
    @allure.step("Проверка открытия модального окна ингредиента")
    def is_ingredient_modal_open(self):
        return self.is_element_visible(self.locators.INGREDIENT_MODAL, timeout=5)
    
    @allure.step("Закрытие модального окна ингредиента")
    def close_ingredient_modal(self):
        close_button = self.wait_and_find_element(self.locators.INGREDIENT_MODAL_CLOSE_BUTTON)
        self.click_to_element_with_script(close_button)
        self.wait_for_modal_close(self.locators.INGREDIENT_MODAL)
    
    @allure.step("Получаем счетчик ингредиента")
    def get_ingredient_counter(self, ingredient):
        counter = ingredient.find_element(*self.locators.INGREDIENT_COUNTER)
        counter_text = counter.text.strip()
        counter_num = int(counter_text)
        
        return counter_num
    
    @allure.step("Добавляем ингредиент в заказ")
    def add_ingredient_to_order(self, ingredient):
        drop_area = self.wait_and_find_element(self.locators.DROP_AREA)
        self.scroll_to_element(ingredient)
        self.drag_and_drop(ingredient, drop_area)
    
    @allure.step("Клик по кнопке 'Оформить заказ'")
    def click_create_order_button(self):
        button = self.wait_for_element_to_be_clickable(self.locators.CREATE_ORDER_BUTTON)
        self.click_to_element_with_script(button)
        
    @allure.step("Оформляем заказ")
    def create_order(self, ingredient):
        self.add_ingredient_to_order(ingredient)
        self.click_create_order_button()
        self.wait_for_page_load()
        self.close_order_modal()
    
    @allure.step("Проверка открытия модального окна заказа")
    def is_order_modal_open(self):
        return self.is_element_visible(self.locators.ORDER_NUMBER_MODAL, timeout=5)
    
    @allure.step("Закрытие модального окна заказа")
    def close_order_modal(self):
        close_button = self.wait_and_find_element(self.locators.ORDER_MODAL_CLOSE_BUTTON)
        self.click_to_element_with_script(close_button)
        self.wait_for_modal_close(self.locators.ORDER_MODAL)
    
    @allure.step("Получаем номер заказа")
    def get_order_number(self):
        order_text = self.get_text_from_element(self.locators.ORDER_NUMBER_MODAL).strip()
        order_num = int(order_text)
        return order_num
    
    @allure.step("Проверка что находимся на главной странице")
    def is_main_page(self):
        return self.get_current_url() == Urls.BASE_URL or self.get_current_url() == f"{Urls.BASE_URL}/"
    
    @allure.step("Проверка видимости секции конструктора")
    def is_constructor_section_visible(self):
        return (self.is_element_visible(self.locators.CONSTRUCTOR_SECTION, timeout=5) or 
                self.is_main_page() or
                self.is_element_visible(self.locators.DROP_AREA, timeout=3))
        
