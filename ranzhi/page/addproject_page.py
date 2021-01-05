from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
import random

class AddProject:

    def add_project(self,uname='admin',pwd='123456'):
        try:
            driver = webdriver.Chrome()
            driver.get('http://localhost/ranzhi/www/')
            driver.maximize_window()
            driver.implicitly_wait(10)

            # 登陆
            driver.find_element_by_id('account').send_keys(uname)
            driver.find_element_by_id('password').send_keys(pwd)
            driver.find_element_by_id('submit').click()
        

            # 点击项目按钮
            driver.find_element_by_id('s-menu-3').click()


            # 进入到frame中
            iframe = driver.find_element_by_id('iframe-3')
            driver.switch_to.frame(iframe)

            
            for i in range(1,5):
                # 点击 添加区块
                driver.find_element_by_xpath('//*[@id="dashboard"]/div[2]/a').click()
                # 选择区块
                blocks = ["task","project"]
                block = blocks[random.randint(0,0)]

                element = driver.find_element_by_id('blocks')
                Select(element).select_by_value(block)

                # 名称
                driver.find_element_by_id('title').send_keys('区块%d'%i)
                # 宽度
                width = driver.find_element_by_id('grid')
                Select(width).select_by_index(random.randint(0,5))
                # 颜色
                driver.find_element_by_xpath('//*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div/button').click()
                driver.find_element_by_xpath('//*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div/div/li[%d]'%(random.randint(1,6))).click()

                # 类型
                driver.find_element_by_id('paramstype_chosen').click()
                driver.find_element_by_xpath('//*[@id="paramstype_chosen"]/div/ul/li[%d]'%(random.randint(1,5))).click()

                # 数量
                driver.find_element_by_id('params[num]').clear()
                driver.find_element_by_id('params[num]').send_keys('20')

                # 排序
                driver.find_element_by_id('paramsorderBy_chosen').click()
                driver.find_element_by_xpath('//*[@id="paramsorderBy_chosen"]/div/ul/li[%d]'%(random.randint(1,6))).click()

                # 任务状态
                driver.find_element_by_id('paramsstatus_chosen').click()
                driver.find_element_by_xpath('//*[@id="paramsstatus_chosen"]/div/ul/li[%d]'%(random.randint(1,6))).click()

                # 保存
                driver.find_element_by_id('submit').click()
                sleep(2)

        finally:
            sleep(3)
            driver.close()

if __name__ == "__main__":
    AddProject().add_project()