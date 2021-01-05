from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
import random
from base.util import BoxDriver,BasePage
from page.login_page import LoginPage

class AddUser(LoginPage):

    # 可不写，
    # def __init__(self,driver):
    #     super().__init__(driver)

    def add_user(self,uname='admin',pwd='123456'):
        try:
            
            driver = self.driver

            # 点击后台管理
            # driver.find_element_by_id('s-menu-superadmin').click()
            driver.click('i,s-menu-superadmin')


            # 进入到frame中
            # iframe = driver.find_element_by_id('iframe-superadmin')
            # driver.switch_to.frame(iframe)
            driver.switch_to_frame('i,iframe-superadmin')
        

            # 点击添加成员
            # driver.find_element_by_xpath('//*[@id="shortcutBox"]/div/div[1]/div/a').click()
            driver.click('x,//*[@id="shortcutBox"]/div/div[1]/div/a')

            for i in range(30,35):
                username = 'user%d'%i
                # 填写成员信息
            #     driver.find_element_by_id('account').send_keys(username)
            #     driver.find_element_by_id('realname').send_keys(username)
            #     driver.find_element_by_id('genderm' if i%2==0 else 'genderf').click()
                driver.input('i,account',username)
                driver.input('i,realname',username)
                driver.click('i,genderm' if i%2==0 else 'i,genderf')
                # driver.click('i,%s'%('genderm' if i%2==0 else 'genderf'))

                # 部门
            #     dept_element = driver.find_element_by_id('dept')
            #     depts = Select(dept_element)
                # 选择部门
            #     depts.select_by_index(random.randint(1,6))
                driver.select_by_index('i,dept',random.randint(1,6))

                # 角色
            #     role_element = driver.find_element_by_id('role')
            #     roles = Select(role_element)
            #     roles.select_by_index(random.randint(1,17))
                driver.select_by_index('i,role',random.randint(1,17))

            #     driver.find_element_by_id('password1').send_keys('123456')
            #     driver.find_element_by_id('password2').send_keys('123456')
            #     driver.find_element_by_id('email').send_keys('%s@163.com'%username)
                driver.input('i,password1','123456')
                driver.input('i,password2','123456')
                driver.input('i,email','%s@163.com'%username)

            #     driver.find_element_by_id('submit').click()
                driver.click('i,submit')
                sleep(2)

                # 跳转到最后一页
            #    driver.find_element_by_id('_pageID').send_keys('10000')
            #     driver.find_element_by_id('goto').click()
                driver.input('i, _pageID','10000')
                driver.click('i,goto')
                sleep(2)

                # 断言
            #     accounts = driver.find_elements_by_xpath('/html/body/div/div/div/div[2]/div/div/table/tbody/tr/td[3]')
                accounts = driver.locate_elements('x,/html/body/div/div/div/div[2]/div/div/table/tbody/tr/td[3]')
                account = accounts[-1]
                assert account.text == username

                # 添加新用户
            #     driver.find_element_by_link_text('添加成员').click()
                driver.click('l,添加成员')
                
        finally:
            sleep(3)
            driver.quit()

if __name__ == "__main__":
    AddUser().add_user()
    # pass