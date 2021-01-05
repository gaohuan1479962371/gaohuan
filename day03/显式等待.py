from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
# 显式等待用的包
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
sleep:   等待指定时间
隐式等待： 等待整个页面加载完成
显式等待： 等待指定元素加载完成
'''

try:
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    driver.maximize_window()

    # driver.find_element_by_id('kw').send_keys('菅义伟')
    # driver.find_element(By.ID,'kw').send_keys('菅义伟')

    # 显示等待
    search = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID, 'kw')))
    search.send_keys('菅义伟')


except Exception as e:
    print(e)
finally:
    sleep(1)
    driver.close()
