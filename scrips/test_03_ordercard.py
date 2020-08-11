import logging
import time
import unittest
from parameterized import parameterized
from config import BAS_URL
from page.commodity_page import CommodityBusiness
from page.home_page import HomeBusiness
from page.login_page import LoginBusiness
from page.shopping_page import ShoppingBusiness
from utils import DriverUtils, transmit_data


class TestOrderCard(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtils.open_driver()
        cls.homepage = HomeBusiness()
        cls.shoppinpage = ShoppingBusiness()

    @classmethod
    def tearDownClass(cls):
        DriverUtils.close_driver()

    def setUp(self):
        self.driver.get('http://127.0.0.1/')

    def tearDown(self):
        pass


    @parameterized.expand(transmit_data(BAS_URL+'./data/Tpshop.json','order_card'))
    def test_03_order_card(self,ordercard):
        self.homepage.home_card()
        message = self.shoppinpage.shopping_card()
        self.assertIn(ordercard,message)
        logging.info("提交成功：{}".format(message))