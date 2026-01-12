import random
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
    
    @allure.step("Ищем элемент")    
    def wait_and_find_element(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
    
    @allure.step("Ищем элементы") 
    def wait_and_find_elements(self, locator, timeout=10, required=False):
        if required:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.presence_of_all_elements_located(locator))
        else:
            try:
                wait = WebDriverWait(self.driver, timeout)
                wait.until(EC.presence_of_all_elements_located(locator))
            except:
                pass
        return self.driver.find_elements(*locator)
    
    @allure.step("Скролл до элемента") 
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    @allure.step("Клик по элементу")
    def click_to_element(self, locator):
        element = self.wait_and_find_element(locator)
        element.click()
    
    @allure.step("Клик по элементу с помощью скрипта")    
    def click_to_element_with_script(self, locator):
        element = self.wait_and_find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)
    
    @allure.step("Получаем текст из элемента")    
    def get_text_from_element(self, locator):
        element = self.wait_and_find_element(locator)
        return element.text
    
    @allure.step("Заполняем поле ввода")
    def send_keys_to_element(self, locator, text):
        element = self.wait_and_find_element(locator)
        element.clear()
        element.send_keys(text)
    
    @allure.step("Получаем рандомный элемент из множества элементов")    
    def get_random_element_in_multiple_elements(self, locator):
        elements = self.wait_and_find_elements(locator)
        element = elements[random.randint(0, len(elements) - 1)]
        return element
    
    @allure.step("Получаем актуальный URL")    
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Проверка элемента на видимость")
    def is_element_visible(self, locator, timeout=5):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
    
    def is_element_present(self, locator, timeout=5):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.presence_of_element_located(locator))
            return True
        except:
            return False
    
    @allure.step("Ждем пока элемент не станет кликабельным")
    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))
    
    @allure.step("Получаем значение атрибута")
    def get_attribute_value(self, locator, attribute):
        element = self.wait_and_find_element(locator)
        return element.get_attribute(attribute)
    
    @allure.step("Перетаскивание элемента (Firefox)")
    def _drag_and_drop_firefox(self, source_element, target_element):
        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];
            
            function createDataTransfer() {
                var dt = new DataTransfer();
                dt.effectAllowed = 'all';
                dt.dropEffect = 'move';
                return dt;
            }
            
            var dataTransfer = createDataTransfer();
            
            var dragStartEvent = new DragEvent('dragstart', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            source.dispatchEvent(dragStartEvent);
            
            var dragEnterEvent = new DragEvent('dragenter', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            target.dispatchEvent(dragEnterEvent);
            
            var dragOverEvent = new DragEvent('dragover', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            dragOverEvent.preventDefault();
            target.dispatchEvent(dragOverEvent);
            
            var dropEvent = new DragEvent('drop', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            dropEvent.preventDefault();
            target.dispatchEvent(dropEvent);
            
            var dragEndEvent = new DragEvent('dragend', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            source.dispatchEvent(dragEndEvent);
        """, source_element, target_element)