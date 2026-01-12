from selenium.webdriver.common.by import By

class ProfilePageLocators:
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    PROFILE_BUTTON = (By.XPATH, "//a[text()='Профиль']")
    ORDER_ITEM_IN_HISTORY = (By.CSS_SELECTOR, "[class*='OrderHistory_listItem__']")
    ORDER_ITEM_NUMBER_IN_HISTORY = (By.XPATH, "//p[@class='text text_type_digits-default']")
