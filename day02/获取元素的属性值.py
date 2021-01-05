from selenium import webdriver
from time import sleep

try:
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    
    # 获取元素的属性值
    href = driver.find_element_by_link_text('新闻').get_attribute('href')
    print(href)
except Exception as e:
    print(e)
finally:
    driver.quit()