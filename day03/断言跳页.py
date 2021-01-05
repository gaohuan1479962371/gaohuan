from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
import random

try:
    driver = webdriver.Chrome()
    driver.get('http://localhost/ranzhi/www/')
    driver.maximize_window()
    driver.implicitly_wait(10)

    # 登陆
    driver.find_element_by_id('account').send_keys('admin')
    driver.find_element_by_id('password').send_keys('123456')
    driver.find_element_by_id('submit').click()
 

    # 点击后台管理
    driver.find_element_by_id('s-menu-superadmin').click()


    # 进入到frame中
    iframe = driver.find_element_by_id('iframe-superadmin')
    driver.switch_to.frame(iframe)
   

    # 点击添加成员
    driver.find_element_by_xpath('//*[@id="shortcutBox"]/div/div[1]/div/a').click()

    for i in range(0,15):
        username = 'user%d'%i
        # username = 'user'+'i'
        # 填写成员信息
        driver.find_element_by_id('account').send_keys(username)
        driver.find_element_by_id('realname').send_keys(username)
        driver.find_element_by_id('genderm' if i%2==0 else 'genderf').click()

        # 部门
        dept_element = driver.find_element_by_id('dept')
        depts = Select(dept_element)
        # 选择部门
        depts.select_by_index(random.randint(1,6))

        # 角色
        role_element = driver.find_element_by_id('role')
        roles = Select(role_element)
        roles.select_by_index(random.randint(1,17))

        driver.find_element_by_id('password1').send_keys('123456')
        driver.find_element_by_id('password2').send_keys('123456')
        driver.find_element_by_id('email').send_keys('%s@163.com'%username)

        driver.find_element_by_id('submit').click()
        sleep(2)

        # 跳转到最后一页
        driver.find_element_by_id('_pageID').send_keys('10000')
        driver.find_element_by_id('goto').click()
        sleep(2)

        # 断言
        accounts = driver.find_elements_by_xpath('/html/body/div/div/div/div[2]/div/div/table/tbody/tr/td[3]')
        account = accounts[-1]
        print(account)
        assert account.text == username

        # 添加新用户
        driver.find_element_by_link_text('添加成员').click()
        
finally:
    sleep(3)
    driver.quit()