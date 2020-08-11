import time

from base.base_driver import BaseDriver, BaseHandles
from base.find_element import FindElement

'''
对象层
'''

class CommodityPage(BaseDriver):

    # 初始化管理
    def __init__(self):
        super().__init__()

    # 商品名连接定位
    def commodity_find_goods(self):
        return self.find_wait(FindElement.commodity_page_goods)

    # 添加购物车按钮定位
    def commodity_find_addcard(self):
        return self.find_wait(FindElement.commodity_page_addcard)

    # 定位到子页面
    def commodity_find_iframe(self):
        return self.find_wait(FindElement.commodity_page_ifram)

    # 定位添加成功文本
    def commodity_find_success(self):
        return self.find_wait(FindElement.commodity_page_text)

    # 定位X号
    def commodity_find_X(self):
        return self.find_wait(FindElement.commodity_page_X)

    # 定位购物车
    def commodity_find_card(self):
        return self.find_wait(FindElement.commodity_page_card)

    # 获取添加购物车后信息
    def commodity_find_rice(self):
        return self.find_wait(FindElement.commodity_page_rice)
'''
操作层
'''
class CommodityHandles(BaseHandles):

    def __init__(self):
        self.commoditypage = CommodityPage()

    # 模拟用户点击商品连接
    def commodity_goods(self):
        self.find_click(self.commoditypage.commodity_find_goods())

    # 模拟用户把商品添加购物车
    def commodity_addcard(self):
        self.find_click(self.commoditypage.commodity_find_addcard())

    # 进入到添加成功子页面,获取成功文本信息
    def commodity_ifarme(self):
        self.find_iframe(self.commoditypage.driver,self.commoditypage.commodity_find_iframe())
        return self.find_text(self.commoditypage.commodity_find_success())

    # 点击子页面X号鼠标移动到购物车获取产品信息
    def commodity_X(self):
        self.find_close_iframe(self.commoditypage.driver)
        self.find_click(self.commoditypage.commodity_find_X())
        time.sleep(2)
        self.find_actions(self.commoditypage.driver,self.commoditypage.commodity_find_card())
        return self.find_text(self.commoditypage.commodity_find_rice())

'''
业务层
'''
class CommodityBusiness:

    def __init__(self):
        self.commodityhandles = CommodityHandles()

    # 点击添加购物商品
    def commodity_add(self):
        self.commodityhandles.commodity_goods()
        time.sleep(2)
        self.commodityhandles.commodity_addcard()
        time.sleep(2)
        return self.commodityhandles.commodity_ifarme()

    # 点击子页面X号鼠标移动到购物车获取产品信息
    def commodity_card(self):
        return self.commodityhandles.commodity_X()