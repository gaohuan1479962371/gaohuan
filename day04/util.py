from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import random


class BoxDriver:

    def __init__(self, browser_type='Chrome'):
        if browser_type == 'Chrome':
            self.driver = webdriver.Chrome()
        elif browser_type == 'Firefox':
            self.driver = webdriver.Firefox()
        elif browser_type == 'Ie':
            self.driver = webdriver.Ie()

    def get(self, url):
        '''
        打开网页
        url:网页的地址
        '''
        self.driver.get(url)

    def maximize_window(self):
        '''
        窗口最大化
        '''
        self.driver.maximize_window()

    def implicitly_wait(self, time=10):
        '''
        隐式等待
        time:最大等待时间，单位是秒，默认等待时间是10
        '''
        self.driver.implicitly_wait(time)

    # 'id,account'-> (By.ID,'account')
    def selector_to_locator(self, selector):
        '''
        把自定义的selector定位方式转换为selenium标准定位方式
        'id,account'-> (By.ID,'account')
        selector: 自定义定位方式
        '''
        # 定位方式
        by = selector.split(',')[0].strip()  # split:以什么方式切分；strip:去掉两端空格字符
        # 定位方式的值
        value = selector.split(',')[1].strip()
        if by == 'id' or by == 'i':
            locator = (By.ID, value)
        elif by == 'name' or by == 'n':
            locator = (By.NAME, value)
        elif by == 'class_name' or by == 'c':
            locator = (By.CLASS_NAME, value)
        elif by == 'link_text' or by == 'l':
            locator = (By.LINK_TEXT, value)
        elif by == 'partial_link_text' or by == 'p':
            locator = (By.PARTIAL_LINK_TEXT, value)
        elif by == 'tag_name' or by == 't':
            locator = (By.TAG_NAME, value)
        elif by == 'xpath' or by == 'x':
            locator = (By.XPATH, value)
        elif by == 'css_selector' or by == 'css':
            locator = (By.CSS_SELECTOR, value)

        return locator

    def locate_element(self, selector):
        '''
        定位单个元素
        selector: 自定义定位方式
        '''
        locator = self.selector_to_locator(selector)
        element = self.driver.find_element(*locator)
        return element

    def locate_elements(self, selector):
        '''
        定位多个元素
        selector: 自定义定位方式
        '''
        locator = self.selector_to_locator(selector)
        elements = self.driver.find_elements(*locator)
        return elements

    def click(self, selector):
        '''
        单击元素
        selector:自定义定位方式
        '''
        self.locate_element(selector).click()

    def input(self, selector, word):
        '''
        向文本框写入值
        selector:自定义定位方式
        '''
        self.locate_element(selector).send_keys(word)

    def quit(self):
        '''
        退出浏览器
        '''
        self.driver.quit()

    def close(self):
        '''
        关闭当前窗口
        '''
        self.driver.close()

    def switch_to_frame(self, selector):
        '''
        进入frame
        '''
        iframe = self.locate_element(selector)
        self.driver.switch_to.frame(iframe)

    def select_by_index(self, selector, index):
        '''
        根据index选择元素
        index：选项的索引
        selector: 自定义定位方式
        '''

        element = self.locate_element(selector)
        selects = Select(element)
        selects.select_by_index(index)

    def select_by_value(self, selector, value):
        '''
        根据value选择元素
        value：选项的索引
        selector: 自定义定位方式
        '''
        element = self.locate_element(selector)
        selects = Select(element)
        selects.select_by_value(random.randint(i, j))

    def select_by_visiable_text(self, selector, text):
        '''
        根据visiable_text选择元素
        visiable_text：选项的索引
        selector: 自定义定位方式
        '''
        element = self.locate_element(selector)
        selects = Select(element)
        selects.select_by_visiable_text(text)


if __name__ == "__main__":
    BoxDriver()
