import logging
import unittest
from parameterized import parameterized
from config import BAS_URL
from page.home_page import HomeBusiness
from page.login_page import LoginBusiness
from utils import DriverUtils, transmit_data


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtils.open_driver()
        cls.homepage = HomeBusiness()
        cls.loginpage = LoginBusiness()

    @classmethod
    def tearDownClass(cls):
        DriverUtils.close_driver()

    def setUp(self):
        self.driver.get('http://127.0.0.1/')

    def tearDown(self):
        pass

    @parameterized.expand(transmit_data(BAS_URL+'./data/Tpshop.json','login'))
    def test_login(self,username,password,code):
        self.homepage.home_login()
        self.loginpage.login_loign(username,password,code)
        logging.info('用户名：%s,密码：%s,验证码：%s' % (username, password, code))
