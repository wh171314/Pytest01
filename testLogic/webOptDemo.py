'''
    定义option参数，供初始化webdriver调用
    1.去自动化控制条
    2.窗口最大化
    3.不记录密码
'''
from selenium import webdriver

def optionConf():
    options = webdriver.ChromeOptions()
    # 去自动化控制条
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 窗口最大化
    options.add_argument('start-maximized')
    # 不记录密码
    prefs = {}
    prefs["credentials_enable_service"] = False
    prefs["profile.password_manager_enabled"] = False
    options.add_experimental_option('prefs', prefs)
    return options