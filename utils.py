import json

from selenium import webdriver

'''
工具类
'''

class DriverUtils:

    # 定义driver属性
    __driver = None
    # 定义开关属性
    __key = True

    # 打开Webdriver驱动方法
    @classmethod
    def open_driver(cls):
        if cls.__driver is None:
            # 初始化驱动
            cls.__driver = webdriver.Chrome()
            # 浏览器最大化
            cls.__driver.maximize_window()
            # 隐式等待
            cls.__driver.implicitly_wait(10)
            return cls.__driver
        else:
            return cls.__driver

    # 修改开关
    @classmethod
    def open_key(cls,key):
        cls.__key = key

    # 关闭浏览器和驱动
    @classmethod
    def close_driver(cls):
        if cls.__driver is not None and cls.__key is True:
            cls.__driver.quit()
            cls.__driver = None

# 引用json数据
def transmit_data(filename,name):
    data_list = []
    with open(filename,'r',encoding='utf-8') as file:
        # 转换json数据
        jsondata = json.load(file)
        # 获取字典的键
        jsonvalues = jsondata.get(name)
        # 获取字典的值添加进列表
        data_list.append(list(jsonvalues.values()))
    # 把列表返回
    return data_list