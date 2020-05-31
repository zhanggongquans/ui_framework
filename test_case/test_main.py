import pytest
import yaml

from page.app import App
from test_case.test_base import TestBase


class TestMain(TestBase):
    @pytest.mark.parametrize("value1,value2", yaml.safe_load(open("../test_case/test_main.yml")))
    def test_main(self, value1, value2):
        self.app.start().main().goto_search()
        print(value1)
        print(value2)

    def test_window(self):
        self.app.start().main().goto_window()



if __name__ == '__main__':
    pytest.main()
