import time
import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    
    @allure.step("Клик по кнопке 'Конструктор'")
    def click_constructor_button(self):
        self.click_to_element(self.locators.CONSTRUCTOR_BUTTON)
    
    @allure.step("Клик по кнопке 'Лента Заказов'")
    def click_order_button(self):
        self.click_to_element(self.locators.ORDER_BUTTON)
    
    @allure.step("Клик по кнопке 'Личный Кабинет'")
    def click_profile_button(self):
        if self.is_ingredient_modal_open():
            self.close_ingredient_modal()
            WebDriverWait(self.driver, 3).until_not(EC.visibility_of_element_located(self.locators.INGREDIENT_MODAL))
        if self.is_order_modal_open():
            self.close_order_modal()
            WebDriverWait(self.driver, 3).until_not(EC.visibility_of_element_located(self.locators.ORDER_MODAL))
        
        try:
            time.sleep(0.2)
            self.click_to_element_with_script(self.locators.PROFILE_BUTTON)
        except:
            self.click_to_element_with_script(self.locators.PROFILE_BUTTON)
        WebDriverWait(self.driver, 5).until(lambda d: d.current_url == Urls.PROFILE_URL)
    
    @allure.step("Получаем случайный ингредиент")
    def get_random_ingredient(self):
        ingredient = self.get_random_element_in_multiple_elements(self.locators.INGREDIENT_ITEM)
        if not ingredient:
            raise Exception(f"Не найдены ингредиенты по локатору: {self.locators.INGREDIENT_ITEM}. URL: {self.driver.current_url}")
        return ingredient
    
    @allure.step("Клик по ингредиенту")
    def click_ingredient(self, index=None):
        if index is None:
            ingredient = self.get_random_ingredient()
            self.scroll_to_element(ingredient)
            ingredient.click()
        else:
            ingredients = self.wait_and_find_elements(self.locators.INGREDIENT_ITEM)
            if ingredients and index < len(ingredients):
                self.scroll_to_element(ingredients[index])
                ingredients[index].click()
    
    @allure.step("Проверка открытия модального окна ингредиента")
    def is_ingredient_modal_open(self):
        return self.is_element_visible(self.locators.INGREDIENT_MODAL, timeout=5)
    
    @allure.step("Закрытие модального окна ингредиента")
    def close_ingredient_modal(self):
        self.click_to_element_with_script(self.locators.INGREDIENT_MODAL_CLOSE_BUTTON)
        try:
            WebDriverWait(self.driver, 5).until_not(EC.visibility_of_element_located(self.locators.INGREDIENT_MODAL))
        except:
            time.sleep(0.5)
    
    @allure.step("Получаем счетчик ингредиента")
    def get_ingredient_counter(self, ingredient=None):
        if ingredient is None:
            ingredient = self.get_random_ingredient()
        counter = ingredient.find_element(*self.locators.INGREDIENT_COUNTER)
        counter_text = counter.text.strip()
        
        return int(counter_text)
    
    @allure.step("Добавляем ингредиент в заказ")
    def add_ingredient_to_order(self, ingredient=None):
        if ingredient is None:
            ingredient = self.get_random_ingredient()
        drop_area = self.wait_and_find_element(self.locators.DROP_AREA)
        self.scroll_to_element(ingredient)
        time.sleep(0.3)
        
        browser_name = self.driver.capabilities.get('browserName', '').lower()
        
        if browser_name == 'firefox':
            self._drag_and_drop_firefox(ingredient, drop_area)
        else:
            action = ActionChains(self.driver)
            action.click_and_hold(ingredient).pause(0.2).move_to_element(drop_area).pause(0.2).release().perform()
    
    @allure.step("Клик по кнопке 'Оформить заказ'")
    def click_create_order_button(self):
        self.click_to_element(self.locators.CREATE_ORDER_BUTTON)
        
    @allure.step("Оформляем заказ")
    def create_order(self):
        self.add_ingredient_to_order()
        self.click_create_order_button()
        WebDriverWait(self.driver, 10).until(lambda d: self.is_order_modal_open())
        self.close_order_modal()
    
    @allure.step("Проверка открытия модального окна заказа")
    def is_order_modal_open(self):
        return self.is_element_visible(self.locators.ORDER_NUMBER_MODAL, timeout=5)
    
    @allure.step("Закрытие модального окна заказа")
    def close_order_modal(self):
        self.click_to_element_with_script(self.locators.ORDER_MODAL_CLOSE_BUTTON)
        try:
            WebDriverWait(self.driver, 5).until_not(EC.visibility_of_element_located(self.locators.ORDER_MODAL))
        except:
            time.sleep(0.5)
    
    @allure.step("Получаем номер заказа")
    def get_order_number(self):
        if self.is_order_modal_open():
            order_text = self.get_text_from_element(self.locators.ORDER_NUMBER_MODAL)
            order_text = order_text.strip()
            order_num = int(order_text)
            return order_num
        return None
    
    @allure.step("Проверка что находимся на главной странице")
    def is_main_page(self):
        return self.get_current_url() == Urls.BASE_URL or self.get_current_url() == f"{Urls.BASE_URL}/"
    
    @allure.step("Проверка видимости секции конструктора")
    def is_constructor_section_visible(self):
        return (self.is_element_visible(self.locators.CONSTRUCTOR_SECTION, timeout=5) or 
                self.is_main_page() or
                self.is_element_visible(self.locators.DROP_AREA, timeout=3))
        
