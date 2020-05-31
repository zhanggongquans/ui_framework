from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Main(BasePage):

    '''
    进入搜索页
    '''
    def goto_search(self):
        # self.find(By.ID, 'tv_search').click()
        self.steps("../page/data.yml")
