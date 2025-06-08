import requests
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from scr.constants import BaseUrl, Endpoints, Ingredients
from scr.helpers import User
from scr.pages.home_page import HomePage
from scr.pages.home_page_header import HeaderPage
from scr.pages.login_page import LoginPage



@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get('https://stellarburgers.nomoreparties.site/')
        yield driver
        driver.quit()
    elif request.param == 'firefox':
        firefox = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        firefox.maximize_window()
        firefox.get('https://stellarburgers.nomoreparties.site/')
        yield firefox
        firefox.quit()


@pytest.fixture
def create_new_user():
    payload = User.create_user()
    response = requests.post(BaseUrl.BASE_URL + Endpoints.CREATE_USER, data=payload)
    yield payload, response
    token = response.json()["accessToken"]
    requests.delete(BaseUrl.BASE_URL + Endpoints.DELETE_USER, headers={"Authorization": token})


@pytest.fixture
def login(driver, create_new_user):
        create_user_data = create_new_user[0]
        header_page = HeaderPage(driver)
        login_page = LoginPage(driver)
        header_page.click_profile_area_button()
        login_page.login(create_user_data["email"], create_user_data["password"])
        home_page = HomePage(driver)
        home_page.wait_load_home_page()


@pytest.fixture
def create_order(create_new_user):
    token = create_new_user[1].json()["accessToken"]
    headers = {'Authorization': token}
    response = requests.post(BaseUrl.BASE_URL + Endpoints.CREATE_ORDER, headers=headers, data=Ingredients.CORRECT_INGREDIENTS_DATA)
    return response.json()["order"]["number"]