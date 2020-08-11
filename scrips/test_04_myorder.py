import logging
import time
import unittest
from parameterized import parameterized
from config import BAS_URL
from page.home_page import HomeBusiness
from page.myorder_page import MyOrderBusiness
from utils import DriverUtils, transmit_data


class TestMyOrder(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtils.open_driver()
        cls.homepage = HomeBusiness()
        cls.myorderpage = MyOrderBusiness()

    @classmethod
    def tearDownClass(cls):
        DriverUtils.close_driver()

    def setUp(self):
        self.driver.get('http://127.0.0.1/')

    def tearDown(self):
        pass

    @parameterized.expand(transmit_data(BAS_URL+'./data/Tpshop.json','my_order'))
    def test_04_my_order(self,myorder):
        self.homepage.home_order()
        time.sleep(3)
        message = self.myorderpage.my_order()
        logging.info(self.assertIn(myorder,message))
        logging.info("支付成功：{}".format(message))