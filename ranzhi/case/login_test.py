from page.login_page import LoginPage
import unittest
from base.util import BoxDriver, GetExcel, GetCsv, GetLogger
from parameterized import parameterized


class LoginTest(unittest.TestCase):
    logger = GetLogger('./report/ranzhi.log')

    @classmethod
    def setUpClass(self):
        self.driver = BoxDriver()
        self.logger.info('打开了浏览器，输入项目网址')
        self.page = LoginPage(self.driver)  # page其实也是个装有浏览器的对象（因为LoginPage类继承了BasePage类的构造函数）

    @classmethod
    def tearDownClass(self):
        self.logger.info('退出浏览器')
        self.driver.quit()

    @parameterized.expand(GetExcel().load(r'./data/data.xlsx', 'login_success'))
    # @parameterized.expand((GetCsv().load(r'./data/homework.csv'))[:4])
    def test_login_success(self, username, password):
        '''登录成功功能测试用例'''
        try:
            self.logger.info('登录项目')
            self.page.login(username, password)
            # 断言
            real_name = self.page.get_login_name()
            self.logger.info('获取到的真名是%s' % real_name)
            # assert element.text == 'admin'
            self.assertEqual(real_name, username, '登陆失败！')
        except:
            raise NameError('测试失败！')
        finally:
            self.page.logout()

        # self.page.login('user14','123456')
        # # 断言
        # real_name = self.page.get_login_name()
        # # assert element.text == 'user0'
        # self.assertEqual(real_name,'user0','登陆失败！')
        # self.page.logout()

    @parameterized.expand(GetExcel().load(r'./data/data.xlsx', 'login_fail'))
    # @parameterized.expand((GetCsv().load(r'./data/homework.csv'))[4:])
    def test_login_fail(self, username, password):
        '''登陆失败功能测试用例'''
        # 断言
        try:
            self.page.login(username, password)
            self.logger.info('登录完毕！')
            tip = self.page.get_fail_tips()
            self.assertEqual(tip, '登录失败，请检查您的成员名或密码是否填写正确。', '断言失败！')
        except:
            self.logger.error('代码出错了，赶紧排查！')
            raise NameError('测试失败！')
        finally:
            self.page.confirm()


if __name__ == "__main__":
    unittest.main()
