from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select

try:
    driver = webdriver.Chrome()
    driver.get('http://localhost/ranzhi/www/')
    driver.maximize_window()

    # 登录
    sleep(2)
    driver.find_element_by_id('account').send_keys('admin')
    driver.find_element_by_id('password').send_keys('123456')
    driver.find_element_by_id('submit').click()
    sleep(2)

    # 点击后台管理
    driver.find_element_by_id('s-menu-superadmin').click()
    sleep(2)
    # 进入frame中():切换窗体
    iframe = driver.find_element_by_id('iframe-superadmin')
    driver.switch_to.frame(iframe)
    # 点击添加成员
    driver.find_element_by_xpath('//*[@id="shortcutBox"]/div/div[1]/div/a').click()
    
    # 填写成员信息
    driver.find_element_by_id('account').send_keys('tomm')
    driver.find_element_by_id('realname').send_keys('tomm')
    driver.find_element_by_id('genderf').click()
    sleep(2)

    ''' 定位下拉列表(通过Select选择器定位)'''
    # 选择部门
    dept_element = driver.find_element_by_id('dept')
    depts = Select(dept_element)
    depts.select_by_value('9')
    # 选择角色
    role_element = driver.find_element_by_id('role')
    roles = Select(role_element)
    roles.select_by_visible_text('项目经理')

    # driver.find_element_by_id('dept').click()
    # sleep(2)
    # driver.find_element_by_xpath('//*[@value="9"]').click()
    # driver.find_element_by_id('role').click()
    # driver.find_element_by_xpath('//*[text()="研发"]').click()

    driver.find_element_by_id('password1').send_keys('123456')
    driver.find_element_by_id('password2').send_keys('123456')
    driver.find_element_by_id('email').send_keys('123451@qq.com')
    driver.find_element_by_id('submit').click()
    sleep(2)

    # 删除成员
    # driver.find_elements_by_link_text('删除')[-1].click()

    # 点击“取消”
    # driver.switch_to.alert.dismiss()
    sleep(2)
    # driver.find_elements_by_link_text('删除')[-1].click()
    sleep(2)  
    # driver.switch_to.alert.accept()   # 确定
    


except Exception as e:
    print(e)
finally:
    sleep(2)
    driver.quit()
