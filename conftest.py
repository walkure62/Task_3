from faker import Faker
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from data import Urls
from pages.login_page import LoginPage
from pages.main_page import MainPage

from api.user_api import UserApi
from helper import generate_random_string, UserHelper

import pytest

@pytest.fixture
def user_data():
    password = generate_random_string(10)
    fake_ru = Faker('ru_RU')
    
    user_data = {
        "email": fake_ru.email(),
        "password": password,
        "name": fake_ru.user_name()
    }
    
    return user_data

@pytest.fixture
def created_user(request, user_data):
    response = UserApi.create_user(user_data)
    token = response.json()['accessToken']
    UserHelper.register_user_for_cleanup(request, token)
    
    return {
        'user_data': user_data,
        'token': token
    }

@pytest.fixture(autouse=True)
def cleanup_user_after_test(request):
    yield
    
    created_users = []
    
    if hasattr(request, 'instance') and request.instance is not None:
        if hasattr(request.instance, 'created_users'):
            created_users = request.instance.created_users
    
    if not created_users and hasattr(request, 'created_users'):
        created_users = request.created_users
    
    for token in created_users:
        UserApi.delete_user(token)
        print(f"Пользователь с токеном {token} удален")
    
@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'firefox':
        driver = webdriver.Firefox()
    elif request.param == 'chrome':
        driver = webdriver.Chrome()
    else:
        raise ValueError(f'Invalid browser: {request.param}')
    
    driver.get(Urls.BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()
    
@pytest.fixture(autouse=False)
def login(driver, created_user):
    main_page = MainPage(driver)
    main_page.click_login_button()
        
    login_page = LoginPage(driver)
    login_page.login(created_user['user_data']['email'], created_user['user_data']['password'])

    WebDriverWait(driver, 10).until(lambda d: d.current_url != Urls.LOGIN_URL)
    yield