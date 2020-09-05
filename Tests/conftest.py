import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["Chrome"], scope="class")
def browserSetup(request):
    if request.param == "Chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.maximize_window()
        driver.delete_all_cookies()
        driver.get("https://qaclickacademy.github.io/protocommerce/")
        ##driver.set_page_load_timeout(120)
        request.cls.driver = driver
        yield
        driver.close()

    # elif request.param == "Firefox":
    # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    # driver.maximize_window()
    # driver.delete_all_cookies()
    # driver.get("https://qaclickacademy.github.io/protocommerce/")
    ##driver.set_page_load_timeout(120)


