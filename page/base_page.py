import yaml
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

    def steps(self, path):
        with open(path, encoding='utf-8') as f:
            steps = yaml.safe_load(f)
        for step in steps:
            if "by" in step.keys():
                element = self.find(step["by"], step["locator"])
            if "action" in step.keys():
                action = step.keys()
                if action == "click":
                    element.click()
