import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage

class TestPasswordRecovery:
    
    @allure.description("Проверка навигации на страницу восстановления пароля")
    def test_navigate_to_forgot_password_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_login_button()
        
        login_page = LoginPage(driver)
        login_page.click_restore_password_button()
        
        forgot_password_page = ForgotPasswordPage(driver)
        assert forgot_password_page.is_forgot_password_page(), "Не удалось перейти на страницу восстановления пароля"
    
    @allure.description("Проверка функциональности восстановления пароля по email")
    def test_enter_email_and_click_recovery(self, driver, created_user):
        main_page = MainPage(driver)
        main_page.click_login_button()
        
        login_page = LoginPage(driver)
        login_page.click_restore_password_button()
        
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.enter_email(created_user['user_data']['email'])
        forgot_password_page.click_restore_button()
        
        assert forgot_password_page.is_reset_password_page(), "Кнопка восстановления не работает"
    
    @allure.description("Проверка активации поля пароля при клике на кнопку показать/скрыть пароль")
    def test_show_hide_password_button_activates_field(self, driver, created_user):
        main_page = MainPage(driver)
        main_page.click_login_button()
        
        login_page = LoginPage(driver)
        login_page.click_restore_password_button()
        
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.enter_email(created_user['user_data']['email'])
        forgot_password_page.click_restore_button()
        
        forgot_password_page.enter_password(created_user['user_data']['password'])
        forgot_password_page.click_show_password_button()
        assert forgot_password_page.is_password_input_active() or forgot_password_page.is_password_field_highlighted(), "Поле пароля не стало активным после клика на кнопку показать/скрыть пароль"
