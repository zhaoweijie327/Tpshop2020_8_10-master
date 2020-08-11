from base.base_driver import BaseDriver, BaseHandles
from base.find_element import FindElement

'''
对象层
'''

class LoginPage(BaseDriver):

    # 初始化管理
    def __init__(self):
        super().__init__()

    # 登陆页面用户框定位
    def login_find_user(self):
        return self.find_wait(FindElement.login_page_user)

    # 登陆页面密码框定位
    def login_find_pwd(self):
        return self.find_wait(FindElement.login_page_pwd)

    # 登陆页面验证码框定位
    def login_find_code(self):
        return self.find_wait(FindElement.login_page_code)

    # 登陆页面登陆框定位
    def login_find_submit(self):
        return self.find_wait(FindElement.login_page_submit)

'''
操作层
'''
class LoginHandles(BaseHandles):

    def __init__(self):
        self.loginpage = LoginPage()

    # 模拟用户输入用户名
    def login_user(self,text):
        self.find_send_keys(self.loginpage.login_find_user(),text)

    # 模拟用户输入密码
    def login_pwd(self, text):
        self.find_send_keys(self.loginpage.login_find_pwd(), text)

    # 模拟用户输入密码
    def login_code(self, text):
        self.find_send_keys(self.loginpage.login_find_code(), text)

    # 模拟用户点击登陆按钮操作
    def login_submit(self):
        self.find_click(self.loginpage.login_find_submit())

'''
业务层
'''
class LoginBusiness:

    def __init__(self):
        self.loginhandles = LoginHandles()

    # 点击首页登陆连接
    def login_loign(self,user,pwd,code):
        self.loginhandles.login_user(user)
        self.loginhandles.login_pwd(pwd)
        self.loginhandles.login_code(code)
        self.loginhandles.login_submit()