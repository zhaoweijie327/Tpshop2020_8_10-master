from base.base_driver import BaseDriver, BaseHandles
from base.find_element import FindElement

'''
对象层
'''

class HomePage(BaseDriver):

    # 初始化管理
    def __init__(self):
        super().__init__()

    # 首页登陆定位
    def home_find_login(self):
        return self.find_wait(FindElement.home_page_login)

    # 首页搜索框定位
    def home_find_searchbox(self):
        return self.find_wait(FindElement.home_page_searchbox)

    # 首页搜索按钮定位
    def home_find_search(self):
        return self.find_wait(FindElement.home_page_search)

    # 首页购物车按钮定位
    def home_find_card(self):
        return self.find_wait(FindElement.home_page_card)

    # 首页我的订单定位
    def home_find_order(self):
        return self.find_wait(FindElement.home_page_order)

'''
操作层
'''
class HomeHandles(BaseHandles):

    def __init__(self):
        self.homepage = HomePage()

    # 模拟用户操作点击登陆连接方法
    def home_click_login(self):
        self.find_click(self.homepage.home_find_login())

    # 模拟用户输入搜索内容方法
    def home_sendkey_search(self,text):
        self.find_send_keys(self.homepage.home_find_searchbox(),text)

    # 模拟用户点击搜索按钮方法
    def home_click_search(self):
        self.find_click(self.homepage.home_find_search())

    # 模拟用户点击购物车
    def home_click_card(self):
        self.find_click(self.homepage.home_find_card())

    # 模拟用户点击我的订单
    def home_click_order(self):
        self.find_click(self.homepage.home_find_order())

'''
业务层
'''
class HomeBusiness:

    def __init__(self):
        self.homehandles = HomeHandles()

    # 点击首页登陆连接
    def home_login(self):
        self.homehandles.home_click_login()

    # 首页搜索商品
    def home_search(self,text):
        self.homehandles.home_sendkey_search(text)
        self.homehandles.home_click_search()

    # 首页点击购物车按钮
    def home_card(self):
        self.homehandles.home_click_card()

    # 首页点击我的订单
    def home_order(self):
        self.homehandles.home_click_order()