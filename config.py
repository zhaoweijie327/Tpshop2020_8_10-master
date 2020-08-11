import logging.handlers
import os

BAS_URL = os.path.abspath(os.path.dirname(__file__))

# 日志方法
def Tpshop_Log():
    # 1.创建日志器
    logger = logging.getLogger()
    # 2.设置日志级别
    logger.setLevel(level=logging.INFO)
    # 3.创建每日生成一个日志文件的处理
    lht = logging.handlers.TimedRotatingFileHandler \
        (filename=BAS_URL + '/log/WebTpshopp.log', when="midnight",
         interval=1, backupCount=3)
    # 4.创建输出控制台的处理
    ls = logging.StreamHandler()
    # 5.创建格式化器
    fmt_name = '%(asctime)s %(levelname)s [%(name)s] ' \
               '[%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt=fmt_name)
    # 6.将格式化器绑定到处理器
    lht.setFormatter(formatter)
    ls.setFormatter(formatter)
    # 7.将处理器绑定到日志器
    logger.addHandler(lht)
    logger.addHandler(ls)