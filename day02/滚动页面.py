from selenium import webdriver
from time import sleep

try:
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    driver.maximize_window()

    driver.find_element_by_id('kw').send_keys('火箭炮')
    driver.find_element_by_id('su').click()
    sleep(2)

    # 滚动页面的JavaScript代码
    code = 'arguments[0].scrollIntoView();'
    # 目标元素
    target = driver.find_element_by_link_text('帮助')
    # 滚动到目标元素
    driver.execute_script(code,target)
    sleep(2)

except Exception as e:
    print(e)
finally:
    driver.quit()