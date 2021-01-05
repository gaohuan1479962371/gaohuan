import os, sys

# 将当前路径添加到系统路径中
sys.path.append(os.getcwd())
import unittest, time
from base.HTMLTestRunner import HTMLTestRunner
from base.util import Email


class TestRunner:

    def runner(self):
        # 创建测试套件
        suite = unittest.TestSuite()
        # 将测试用例添加到测试套件中
        # 参数1，用例所在的路径
        # 参数2，用例文件应满足的条件
        suite.addTests(unittest.TestLoader().discover('./case', pattern='login_test.py'))

        # 创建html报告文件
        timestr = time.strftime('%Y-%m-%d_%H-%M-%S')  # 时间戳
        path = './report/report_%s.html' % timestr
        report = open(path, mode='wb')
        # 创建用例运行器
        test_runner = HTMLTestRunner(stream=report, title='RanZhi自动化测试报告', description='报告的详细描述')

        # 运行测试用例，生成报告
        test_runner.run(suite)
        # 发送邮件
        Email().send('ranzhi自动化测试报告', path)


if __name__ == "__main__":
    TestRunner().runner()