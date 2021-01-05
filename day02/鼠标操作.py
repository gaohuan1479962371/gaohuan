from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

try:
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    driver.maximize_window()
    sleep(2)
    '''操作鼠标'''
    # 右击
    # search = driver.find_element_by_id('kw')
    # ActionChains(driver).context_click(search).perform()
    # sleep(2)

    # 左击(单击)
    # driver.find_element_by_id('kw').send_keys('人民币汇率升值')
    # btn = driver.find_element_by_id('su')
    # ActionChains(driver).click(btn).perform()
    # sleep(3)
    
    # 双击
    # search = driver.find_element_by_id('kw')
    # ActionChains(driver).double_click(search).perform()
    # sleep(2)

    # 悬停
    # setting = driver.find_element_by_id('s-usersetting-top')
    # ActionChains(driver).move_to_element(setting).perform()
    # sleep(2)

    # senior = driver.find_element_by_link_text('高级搜索')
    # ActionChains(driver).click(senior).perform()
    # sleep(2)

    # 按住不放
    driver.find_element_by_id('kw').send_keys('青岛疫情')
    driver.find_element_by_id('su').click()
    sleep(2)
    # link = driver.find_element_by_partial_link_text('知乎')
    # ActionChains(driver).click_and_hold(link).perform()
    # sleep(2)

    search = driver.find_element_by_id('kw')
    search.send_keys(Keys.CONTROL,'a')
    search.send_keys(Keys.CONTROL,'c')
    search.send_keys(Keys.CONTROL,'v')
    search.send_keys(Keys.CONTROL,Keys.SHIFT,'v')
    search.send_keys(Keys.CONTROL,Keys.SHIFT,'v')
    search.click()

    search.send_keys(Keys.CONTROL,Keys.SHIFT,'i')
    sleep(2)



except Exception as e:
    print(e)
finally:
    driver.quit()
