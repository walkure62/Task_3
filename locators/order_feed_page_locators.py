from selenium.webdriver.common.by import By

class OrderPageLocators:
    ORDER_ITEM_IN_FEED = (By.CSS_SELECTOR, "[class*='OrderHistory_orderItem__'], [class*='OrderFeed_orderItem__'], [class*='orderItem__'], a[href*='/feed/']")
    ORDER_ITEM_NUMBER_IN_FEED = (By.XPATH, "//p[@class='text text_type_digits-default']")
    ORDER_FEED_MODAL = (By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//div[@class='Modal_modal__container__Wo2l_']")
    ORDER_COUNTER_ALL_TIME = (By.XPATH, "//p[contains(text(), 'Выполнено за все время')]/following-sibling::p[contains(@class, 'OrderFeed_number__')]")
    ORDER_COUNTER_TODAY = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p[contains(@class, 'OrderFeed_number__')]")
    ORDER_LIST_READY = (By.CSS_SELECTOR, "[class*='OrderFeed_orderListReady__']")
    ORDER_LIST_IN_PROGRESS = (By.CSS_SELECTOR, "[class*='OrderFeed_orderListInProgress__']")
    ORDER_NUMBER_IN_PROGRESS = (By.XPATH, "//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']//li")
    ORDER_NUMBER_IN_FEED_MODAL = (By.CSS_SELECTOR, "[class*='Modal_orderNumber__']")
    ORDER_FEED_MODAL_CLOSE_BUTTON = (By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")