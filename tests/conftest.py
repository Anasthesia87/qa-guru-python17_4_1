import pytest
from selene import browser
#from selene import browser as selene_browser, Browser, Config
#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://todomvc.com/examples/emberjs/todomvc/dist'
    browser.config.timeout = 2.0
    browser.config.driver_name = 'chrome'
    #selene_browser.config.type_by_js = True
    #selene_browser.config.click_by_js = True
    #browser.config.build_driver_strategy
    #driver_options = webdriver.FirefoxOptions()
    #driver_options.add_argument('--headless') невидимый режим браузера
    #browser.config.driver_options = driver_options
    #browser.config.driver = webdriver.Chrome  создать драйвер???
    #service=ChromeService(executable_path=ChromeDriverManager().install()), создать драйвер???
    #options=driver_options, создать драйвер???
    #) создать драйвер???

    yield

    browser.quit()