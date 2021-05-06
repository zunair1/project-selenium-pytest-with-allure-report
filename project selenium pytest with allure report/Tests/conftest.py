import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='class')
def init_driver(request):
    options = Options()
    options.headless = False
    request.cls.driver = webdriver.Chrome(executable_path="D:/SeleniumPyTest/chromedriver_win32/chromedriver.exe",
                                  options=options)
    request.cls.driver.get("https://microaccounttest.ihpapp.com/")
    request.cls.driver.maximize_window()
    yield
    request.cls.driver.quit()