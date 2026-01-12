from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    RESTORE_PASSWORD_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")