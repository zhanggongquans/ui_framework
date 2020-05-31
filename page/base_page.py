import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    '''
    定义基础类
    '''
    _driver: WebDriver
    _black_list = [(By.ID, "iv_close")]

    '''
    初始化 driver
    '''

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    '''
    公共配置在po里面封装
    '''

    def find(self, locator, value):
        try:
            element = self._driver.find_element(locator, value)
            return element
        except:
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    break
            #c处理完黑名单后继续寻找元素
            return self.find(locator, value)

    def click(self, locator, value):
        return self._driver.find_element(locator, value).click()

    '''
    测试步骤的封装
    '''

    def steps(self, path):
        with open(path, encoding='utf-8') as f:
            steps = yaml.safe_load(f)
        for step in steps:
            if "by" in step.keys():
                element = self.find(step["by"], step["locator"])
            if "action" in step.keys():
                action = step["action"]
                if action == "click":
                    element.click()
