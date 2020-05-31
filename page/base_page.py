from appium.webdriver.webdriver import WebDriver


class BasePage:
    '''
    定义基础类
    '''
    _driver: WebDriver

    '''
    初始化 driver
    '''
    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    '''
    封装find方法
    '''
    def find(self, locator, value):
        return self._driver.find_element(locator, value)
