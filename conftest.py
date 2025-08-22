import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config.data import Data
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.personal_page import PersonalPage


# эта фикстура будет создавать экземпляр драйвера для каждого теста отдельно:
@pytest.fixture(scope="function", autouse=True)
def driver(request):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920, 1080")
    driver = webdriver.Chrome(options=options)
    #     данная конструкция создает объкет драйвера внутри тестовых классов, внутри наших тестов:
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def setup(request, driver):
    request.cls.data = Data()
    request.cls.login_page = LoginPage(driver)
    request.cls.dashboard_page = DashboardPage(driver)
    request.cls.personal_page = PersonalPage(driver)