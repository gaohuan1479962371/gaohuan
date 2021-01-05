from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains    #鼠标操作相关包
from selenium.webdriver.common.keys import Keys                     #键盘操作相关包
from selenium.webdriver.support.select import Select                #菜单选择器相关包

try:
    driver = webdriver.Chrome()
    driver.get('http://localhost/ranzhi/www/')
    driver.maximize_window()
    sleep(2)
    driver.find_element_by_id('account').send_keys('admin')
    driver.find_element_by_id('password').send_keys('123456')
    driver.find_element_by_id('password').send_keys(Keys.ENTER)
    sleep(2)
    driver.find_element_by_id('s-menu-superadmin').click()
    sleep(2)
    iframe = driver.find_element_by_id('iframe-superadmin')
    driver.switch_to.frame(iframe)
    sleep(2)
    driver.find_element_by_link_text('组织').click()
    sleep(2)

    for i in range(3):
        driver.find_elements_by_link_text('删除')[-1].click()
        sleep(2)
        driver.switch_to.alert.accept()
        sleep(2)

except Exception as e:
    print(e)
finally:
    sleep(2)
    driver.quit()