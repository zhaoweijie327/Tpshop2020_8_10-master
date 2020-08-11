'''
基类
'''
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from utils import DriverUtils


class BaseDriver:

    # 初始化管理工具类的open_driver方法
    def __init__(self):
        self.driver = DriverUtils.open_driver()

    # 定位元素方法(1)
    def find_element(self,loc):
        return self.driver.find_element(*loc)

    # 定位一组元素方法(1)
    def find_elements(self,loc):
        return self.driver.find_elements(*loc)

    # 显式定位元素方法
    def find_wait(self,loc,time=10,wait=1.0):
        return WebDriverWait(self.driver,time,wait).until(lambda find_element:find_element.find_element(*loc))

    # 显式定位一组元素方法
    def find_waits(self,loc,time=10,wait=1.0):
        return WebDriverWait(self.driver,time,wait).until(lambda find_element:find_element.find_elements(*loc))

class BaseHandles:

    # def __init__(self):
    #     self.driver = DriverUtils.open_driver()

    # 模拟用户输入方法
    def find_send_keys(self,element,text):
        element.clear()
        element.send_keys(text)

    # 模拟用户点击操作
    def find_click(self,element):
        element.click()

    # 获取文本信息
    def find_text(self,element):
        return element.text

    # 跳转子页面
    def find_iframe(self,driver,element):
        driver.switch_to.frame(element)

    # 跳转子页面
    def find_close_iframe(self, driver):
        driver.switch_to.default_content()

    # 鼠标移动悬浮操作
    def find_actions(self,driver,element):
        ActionChains(driver).move_to_element(element).perform()

    # 窗口滚动条操作
    def find_windows(self,driver):
        js = "window.scrollTo(0,1000000)"
        driver.execute_script(js)

    # 跳转新窗口
    def find_new_windows(self,driver):
        list = driver.window_handles
        driver.switch_to.window(list[-1])