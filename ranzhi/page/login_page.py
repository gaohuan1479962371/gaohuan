from base.util import BoxDriver, BasePage
import yaml
from base.util import GetYaml
from time import sleep


class LoginPage(BasePage):

    # 用户名和密码参数化
    def login(self, username='admin', password='123456'):
        '''登陆操作流程'''
        config = GetYaml().load(r'./data/config.yaml')
        driver = self.driver
        driver.input(config['LoginPage']['account'], username)
        driver.input(config['LoginPage']['password'], password)
        driver.click(config['LoginPage']['submit'])
        sleep(1)
        # return driver

    def logout(self):
        driver = self.driver
        # 退出
        driver.click('l,签退')
        driver.wait(1)

    def confirm(self):
        driver = self.driver
        # 登陆失败时点击“确认”
        driver.click('x,/html/body/div[2]/div/div/div[2]/button')
        driver.wait(1)

    def get_login_name(self):
        element = self.driver.locate_element('x,//*[@id="mainNavbar"]/div/ul[1]/li/a')
        return element.text

    def get_fail_tips(self):
        element = self.driver.locate_element('x,/html/body/div[2]/div/div/div[1]/div')
        return element.text


if __name__ == "__main__":
    # file = r'E:\workspace\selenium\ranzhi\config.yaml'
    # with open(file,'r',encoding='utf-8') as yaml_file:
    #     config = yaml.load(yaml_file.read(),Loader=yaml.BaseLoader)
    #     print(config)
    LoginPage(BoxDriver()).login()
