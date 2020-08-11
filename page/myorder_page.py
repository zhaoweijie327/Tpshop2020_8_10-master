import time

from base.base_driver import BaseDriver, BaseHandles
from base.find_element import FindElement

'''
对象层
'''

class MyOrderPage(BaseDriver):

    # 初始化管理
    def __init__(self):
        super().__init__()

    # 待付款定位
    def myorder_find_payment(self):
        return self.find_wait(FindElement.myorder_page_payment)

    # 立即支付定位
    def myorder_find_immediately(self):
        return self.find_wait(FindElement.myorder_page_immediately)

    # 货到付款定位
    def myorder_find_cod(self):
        return self.find_wait(FindElement.myorder_page_cod)

    # 支付订单定位
    def myorder_find_confirm(self):
        return self.find_wait(FindElement.myorder_page_confirm)

   # 付款成功定位
    def myorder_find_success(self):
        return self.find_wait(FindElement.myorder_page_success)


'''
操作层
'''
class MyOrderHandles(BaseHandles):

    def __init__(self):
        self.myorderpage = MyOrderPage()

    # 模拟用户操作点击待付款
    def myorder_click_payment(self):
        time.sleep(2)
        self.find_new_windows(self.myorderpage.driver)
        self.find_click(self.myorderpage.myorder_find_payment())

    # 模拟用户点击立即支付
    def myorder_click_immediately(self):
        self.find_click(self.myorderpage.myorder_find_immediately())

    # 模拟用户点击货到付款
    def myorder_click_cod(self):
        time.sleep(2)
        self.find_new_windows(self.myorderpage.driver)
        self.find_click(self.myorderpage.myorder_find_cod())

    # 模拟用户点击确认付款
    def myorder_click_confirm(self):
        time.sleep(3)
        self.find_click(self.myorderpage.myorder_find_confirm())

    # 获取支付成功文本
    def myorder_text_success(self):
        return self.find_text(self.myorderpage.myorder_find_success())


'''
业务层
'''
class MyOrderBusiness:

    def __init__(self):
        self.myorderhandles = MyOrderHandles()

    # 点击购物车提交订单
    def my_order(self):
        self.myorderhandles.myorder_click_payment()
        self.myorderhandles.myorder_click_immediately()
        self.myorderhandles.myorder_click_cod()
        self.myorderhandles.myorder_click_confirm()
        return self.myorderhandles.myorder_text_success()
