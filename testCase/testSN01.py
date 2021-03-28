
# import unittest
from time import sleep

import pytest
import allure
from ddt import ddt,file_data

from testLogic.webKeyDemo import WK


# class testSN01(unittest.TestCase):
@ddt
class testSN01:
    @classmethod
    def setup_class(cls) -> None:
        cls.wk = WK('Chrome')
    @classmethod
    def teardown_class(cls) -> None:
        cls.wk.quit()

    # def setUp(self) -> None:
    #     self.wk = WK('Chrome')
    # def tearDown(self) -> None:
    #     self.wk.quit()

    # 食品-纯牛奶品类下搜索品牌，加入购物车进行结算
    @allure.feature('测试场景01')
    @allure.story('食品-纯牛奶品类下搜索品牌，加入购物车进行结算')
    @allure.title('测试用例01')
    @file_data('../testData/testSN01_food.yaml')
    def test_01(self,**kwargs):
        # 打开url-悬停食品-点击纯牛奶-切换窗体-输入品牌-点击搜索-点击加入购物车-悬停右侧购物车-点击购物车-点击结算-点击支付
        self.wk.open(kwargs['url_'])
        self.wk.moveto(**kwargs['food'])
        self.wk.click(**kwargs['milk'])
        self.wk.switch_handle()
        self.wk.input(**kwargs['band'])
        self.wk.click(**kwargs['searchS'])
        self.wk.click(**kwargs['addCart'])
        self.wk.moveto(**kwargs['Cart'])
        self.wk.click(**kwargs['Cart'])
        sleep(4)
        self.wk.click(**kwargs['settle'])
        self.wk.click(**kwargs['checkout'])

if __name__ == '__main__':
    pytest.main()
