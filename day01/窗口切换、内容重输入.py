from selenium import webdriver
from time import sleep

try:
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    # 窗口最大化
    driver.maximize_window()
    sleep(2)
    # 窗口最小化
    # driver.minimize_window()
    # sleep(2)
    # 获取窗口尺寸
    size = driver.get_window_size()
    print('窗口尺寸=%s'%size)

    driver.find_element_by_id('kw').send_keys('python')
    sleep(1)
    driver.find_element_by_id('kw').send_keys('java')

    # 清除输入框
    sleep(2)
    driver.find_element_by_id('kw').clear()
    driver.find_element_by_id('kw').send_keys('java')
    driver.find_element_by_id('su').click()
    # 点击“百度百科”
    sleep(2)
    driver.find_element_by_partial_link_text('百度百科').click()
    sleep(2)

    # 获取窗口句柄（把手）
    handles = driver.window_handles
    # print(handles)
    # 切换窗口
    driver.switch_to.window(handles[1])
    # 点击“讨论”
    sleep(2)
    # driver.find_element_by_partial_link_text('讨论').click()
    driver.find_element_by_xpath('//*[contains(text(),"讨论")]').click()
except Exception as e:
    print(e)
finally:
    sleep(3)
    driver.quit()
