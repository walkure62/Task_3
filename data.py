class Urls:
    BASE_URL = "https://stellarburgers.education-services.ru"
    PROFILE_URL = f'{BASE_URL}/account/profile'
    ORDER_HISTORY_URL = f'{BASE_URL}/account/order-history'
    LIST_OF_ORDERS_URL = f'{BASE_URL}/feed'
    LOGIN_URL = f'{BASE_URL}/login'
    FORGOT_PASSWORD_URL = f'{BASE_URL}/forgot-password'
    RESET_PASSWORD_URL = f'{BASE_URL}/reset-password'
    CREATE_USER_URL = BASE_URL + '/api/auth/register'
    DELETE_USER_URL = BASE_URL+ '/api/auth/user'
