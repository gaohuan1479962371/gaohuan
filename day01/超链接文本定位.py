from selenium import webdriver
from time import sleep

try:

    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')

    '''打开新闻页面'''
    # news = driver.find_element_by_class_name('mnav')
    # news.click()

    '''利用超链接的文本进行精确定位'''
    # 打开视频页面
    # vedio = driver.find_element_by_link_text('视频')
    # vedio.click()
    '''利用超链接的文本进行模糊定位'''
    # 打开贴吧
    driver.find_element_by_partial_link_text('贴').click()
except Exception as e:
    print(e)
finally: 
    sleep(2)
    driver.quit()
