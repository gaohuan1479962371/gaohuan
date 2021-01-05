from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


class BoxDriver:

    def __init__(self, browser_type='chrome'):
        if browser_type == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser_type == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser_type == 'ie':
            self.driver = webdriver.Ie()
        elif browser_type == 'opera':
            self.driver = webdriver.Opera()

    def get(self, url):
        self.driver.get(url)

    def maximize_window(self):
        self.driver.maximize_window()

    def implicitly_wait(self, time=10):
        self.driver.implicitly_wait(time)

    def selector_locator(self, selector):
        by = selector.split(',')[0].strip()
        value = selector.split(',')[1].strip()

        if by in ['id', 'ID', 'i', 'I']:
            locator = (By.ID, value)
        elif by in ['name', 'NAME', 'n', 'N']:
            locator = (By.NAME, value)
        elif by in ['class_name', 'CLASS-NAME', 'c', 'C']:
            locator = (By.CLASS_NAME, value)
        elif by in ['tag_name', 'TAG_NAME', 'T', 't']:
            locator = (By.TAG_NAME, value)
        elif by in ['link_text', 'LINK_TEXT', 'l', 'L']:
            locator = (By.LINK_TEXT, value)
        elif by in ['partical_link_text', 'PARTICAL_LINK_TEXT', 'P', 'p']:
            locator = (By.PARTIAL_LINK_TEXT, value)
        elif by in ['xpath', 'XPATH', 'x', 'X']:
            locator = (By.XPATH, value)
        elif by in ['css_selector', 'CSS_SELECTOR', 'CSS', 'css']:
            locator = (By.CSS_SELECTOR, value)

        return locator

    def locate_element(self, selector):
        locator = self.selector_locator(selector)
        element = self.driver.find_element(*locator)
        return element

    def input(self, selector, word):

        self.locate_element(selector).send_keys(word)

    def click(self, selector):
        self.locate_element(selector).click()

    def quit(self):
        self.driver.quit()

    def close(self):
        self.driver.close()


if __name__ == "__main__":
    BoxDriver()
