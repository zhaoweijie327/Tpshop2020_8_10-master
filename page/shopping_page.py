import time

from base.base_driver import BaseDriver, BaseHandles
from base.find_element import FindElement

'''
对象层
'''

class ShoppingPage(BaseDriver):

    # 初始化管理
    def __init__(self):
        super().__init__()

    # 结算按钮定位
    def shopping_find_card(self):
        return self.find_wait(FindElement.shopping_page_card)

    # 提交订单按钮定位
    def shopping_find_order(self):
        return self.find_wait(FindElement.shopping_page_place_order)

    # 提交成功信息定位
    def shopping_find_text(self):
        return self.find_wait(FindElement.shopping_page_text)


'''
操作层
'''
class ShoppingHandles(BaseHandles):

    def __init__(self):
        self.shoppingpage = ShoppingPage()

    # 模拟用户操作点击结算方法
    def shopping_click_card(self):
        self.find_click(self.shoppingpage.shopping_find_card())
        time.sleep(3)

    # 模拟用户点击提交
    def shopping_click_order(self):
        self.find_windows(self.shoppingpage.driver)
        self.find_click(self.shoppingpage.shopping_find_order())

    # 模拟用户点击搜索按钮方法
    def shopping_text(self):
        return self.find_text(self.shoppingpage.shopping_find_text())


'''
业务层
'''
class ShoppingBusiness:

    def __init__(self):
        self.shoppinghandles = ShoppingHandles()

    # 点击购物车提交订单
    def shopping_card(self):
        self.shoppinghandles.shopping_click_card()
        self.shoppinghandles.shopping_click_order()
        return self.shoppinghandles.shopping_text()
