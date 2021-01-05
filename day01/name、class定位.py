from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

'''name定位'''
input = driver.find_element_by_name('wd')
input.send_keys("台海登录")

'''tag_name定位'''
input = driver.find_element_by_tag_name('input')
input.send_keys('台风登陆')

'''class定位'''
btn = driver.find_element_by_class_name('s_btn')
btn.click()


sleep(3)
# 关闭当前窗口
driver.close()
# 退出浏览器
drive.quit()