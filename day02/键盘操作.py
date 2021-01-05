from selenium import webdriver
from time import sleep

from selenium.webdriver.common.keys import Keys

'''键盘和鼠标操作'''

try:
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    driver.maximize_window()
    search = driver.find_element_by_id('kw')
    search.send_keys('福建')
    sleep(2)
    # 按一下回车键
    search.send_keys(Keys.ENTER)
    sleep(2)
    # 全选搜索框内容
    search.send_keys(Keys.CONTROL, 'a')
    sleep(2)
    # 复制搜索框内容
    search.send_keys(Keys.CONTROL, 'C')
    sleep(2)
    # 粘贴搜索框内容
    # search.clear()
    driver.refresh()
    sleep(2)
    search.send_keys(Keys.CONTROL, 'v')
    search.send_keys(Keys.CONTROL, 'v')
    search.send_keys(Keys.CONTROL, 'v')
    sleep(2)
except Exception as e:
    print(e)
finally:
    driver.quit()
