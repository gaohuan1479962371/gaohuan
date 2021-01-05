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
            driver.find_element_by_id('account').send_keys(uname)
            driver.find_element_by_id('password').send_keys(pwd)
            driver.find_element_by_id('submit').click()

            driver.find_element_by_xpath('//*[@id="s-menu-3"]/button/img').click()
            iframe = driver.find_element_by_id('iframe-3')
            driver.switch_to.frame(iframe)

            for i in range(0,5):

                driver.find_element_by_xpath('//*[@id="dashboard"]/div[2]/a').click()

                # 选择区块
                block_element = driver.find_element_by_id('blocks')
                blocks = Select(block_element)
                block = random.randint(1,2)
                blocks.select_by_index(block)
                
                # 区块名称
                driver.find_element_by_id('title').send_keys('python%s'%i)

                # 外观宽度
                grid_element = driver.find_element_by_id('grid')
                grids = Select(grid_element)
                grids.select_by_index(random.randint(0,5))
                # 外观颜色
                driver.find_element_by_xpath('//*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div').click()
                a = random.randint(1,6)
                driver.find_element_by_xpath('//*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div/div/li[%d]/button'%a).click()
                if block == 1:
                    # 类型
                    driver.find_element_by_xpath('//*[@id="paramstype_chosen"]').click()
                    t = random.randint(1,5)
                    driver.find_element_by_xpath('//*[@id="paramstype_chosen"]/div/ul/li[%d]'%t).click()
                else:
                    # 状态
                    driver.find_element_by_xpath('//*[@id="paramsstatus_chosen"]').click()
                    tt = random.randint(1,4)
                    driver.find_element_by_xpath('//*[@id="paramsstatus_chosen"]/div/ul/li[%d]'%tt).click()
                # 数量
                driver.find_element_by_id('params[num]').send_keys(i)

                if block == 1:
                    # 排序
                    driver.find_element_by_xpath('//*[@id="paramsorderBy_chosen"]').click()
                    j = random.randint(1,6)
                    driver.find_element_by_xpath('//*[@id="paramsorderBy_chosen"]/div/ul/li[%d]'%j).click()
        
                    # 任务状态
                    driver.find_element_by_xpath('//*[@id="paramsstatus_chosen"]').click()
                    z = random.randint(1,6)
                    driver.find_element_by_xpath('//*[@id="paramsstatus_chosen"]/div/ul/li[%d]'%z).click()
                else:
                    # 排序
                    driver.find_element_by_xpath('//*[@id="paramsorderBy_chosen"]').click()
                    zz = random.randint(1,6)
                    driver.find_element_by_xpath('//*[@id="paramsorderBy_chosen"]/div/ul/li[%d]'%zz).click()

                driver.find_element_by_id('submit').click()
                sleep(2)

        finally:
            sleep(2)
            driver.quit()

if __name__ == "__main__":
    AddProject().add_project()
