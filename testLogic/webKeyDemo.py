from time import sleep
import logging
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from testLogic.webOptDemo import optionConf


def Broswer(type_):
    # 接收浏览器类型，传递option配置，返回浏览器driver对象
    driver = getattr(webdriver, type_)(options=optionConf())
    return driver


class WK:
    # 定义driver
    # driver = webdriver.Chrome()

    # 构造函数，将浏览器对象进行初始化
    def __init__(self, type_):
        self.driver = Broswer(type_)

    # 打开网址
    def open(self, url_):
        self.driver.get(url_)

    # 关闭浏览器
    def quit(self):
        sleep(4)
        self.driver.quit()

    def sleep(self):
        sleep(1)

    # 定位元素
    def locator(self, **kwargs):
        return self.driver.find_element(kwargs['name'], kwargs['value'])

    # 文本框输入,或上传文件
    def input(self, **kwargs):
        self.locator(**kwargs).send_keys(kwargs['txt'])

    # 点击操作
    def click(self, **kwargs):
        self.locator(**kwargs).click()

    # ActionChains鼠标移动至
    def moveto(self,**kwargs):
        el = self.locator(**kwargs)
        ActionChains(self.driver).move_to_element(el).perform()
        sleep(1)

    # 显示等待，查找定位元素
    def assert_wait(self, **kwargs):
        try:
            return WebDriverWait(self.driver, kwargs['txt'], 0.5).until(
                lambda el: self.locator(**kwargs))
        except:
            return False

    # 切换窗体
    def switch_handle(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
    # 切换回前窗体
    def switch_handleback(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])
    # 切换iframe
    def switch_iframe(self, **kwarges):
        iframe = self.locator(**kwarges)
        self.driver.switch_to.frame(iframe)
    # 从iframe切回
    def switch_iframeback(self):
        self.driver.switch_to.default_content()
