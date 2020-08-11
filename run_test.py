import unittest

from config import BAS_URL
from utils import DriverUtils

start = unittest.TestLoader().discover(BAS_URL+'./scrips',pattern='test*.py')

DriverUtils.open_key(False)

runner = unittest.TextTestRunner()
runner.run(start)

DriverUtils.open_key(True)
DriverUtils.close_driver()