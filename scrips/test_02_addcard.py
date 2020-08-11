import logging
import time
import unittest
from parameterized import parameterized
from config import BAS_URL
from page.commodity_page import CommodityBusiness
from page.home_page import HomeBusiness
from utils import DriverUtils, transmit_data


class TestAddCard(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverUtils.open_driver()
        cls.homepage = HomeBusiness()
        cls.commoditypage = CommodityBusiness()

    @classmethod
    def tearDownClass(cls):
        DriverUtils.close_driver()

    def setUp(self):
        time.sleep(3)
        self.driver.get('http://127.0.0.1/')


    @parameterized.expand(transmit_data(BAS_URL+'./data/Tpshop.json','goods_name'))
    def test_add_card(self,name,sussces,goods):
        self.homepage.home_search(name)
        msg = self.commoditypage.commodity_add()
        self.assertIn(sussces,msg)
        message = self.commoditypage.commodity_card()
        self.assertIn(goods,message)
        logging.info('搜索名称：%s' % name)
        logging.info("添加成功：{}".format(msg))
        logging.info("添加商品是：{}".format(message))