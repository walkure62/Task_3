from selenium.webdriver.common.by import By

class ForgotPasswordPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon')] | //div[contains(@class, 'input__action')]")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    PASSWORD_INPUT_ACTIVE = (By.XPATH, "//input[@type='text' and contains(@class, 'input__textfield')]")
    SAVE_PASSWORD_BUTTON = (By.XPATH, "//button[text()='Сохранить']")