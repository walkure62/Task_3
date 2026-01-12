import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage

class TestProfile:
    
    @allure.description("Проверка навигации в личный кабинет")
    def test_navigate_to_profile(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_profile_button()
        
        profile_page = ProfilePage(driver)
        assert profile_page.is_profile_page(), "Не удалось перейти в личный кабинет"
    
    @allure.description("Проверка навигации в раздел 'История заказов'")
    def test_navigate_to_order_history(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_profile_button()
        
        profile_page = ProfilePage(driver)
        assert profile_page.is_profile_page(), "Не удалось перейти в личный кабинет"
        
        profile_page.click_order_history_button()
        assert profile_page.is_order_history_page(), "Не удалось перейти в раздел 'История заказов'"
    
    @allure.description("Проверка выхода из аккаунта")
    def test_logout(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_profile_button()
        
        profile_page = ProfilePage(driver)
        assert profile_page.is_profile_page(), "Не удалось перейти в личный кабинет"
        
        profile_page.click_logout_button()
        assert profile_page.is_logged_out(), "Не удалось выйти из аккаунта"
