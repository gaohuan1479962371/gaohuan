from selenium import webdriver
from time import sleep

try:
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    '''CSS 定位'''
    driver.find_element_by_css_selector('#kw').send_keys('C')
    driver.find_element_by_css_selector('#su').click()
    # 标准CSS路径
    # hotsearch-content-wrapper > li:nth-child(6) > a > span.title-content-title
except Exception as e:
    print(e)
finally:
    sleep(3)
    driver.quit()
