import unittest

'''单元测试'''


# 单元测试类必须继承TestCase类
# 执行的方法的顺序按方法名的ASII码从小到大执行
class Test01(unittest.TestCase):

    # setUpClass()方法在所有方法前面执行，并且执行一次
    @classmethod  # @：表示注解   classmethod: 告诉机器底下的方法是类方法且只运行一次
    def setUpClass(self):
        print('------START------')

    # tearDownClass()方法在所有方法最后执行，并且执行一次
    @classmethod
    def tearDownClass(self):
        print('------END--------')

    def setUp(self):
        print('方法要开始执行了...')

    def tearDown(self):
        print('方法结束了...')

    def testrun(self):
        # print('方法要开始执行了...')
        print('这是run()方法')

    # 用例方法必须以test开头
    def test01(self):
        # print('方法要开始执行了...')
        print('这是test01()方法...')

    def test02(self):
        # print('方法要开始执行了...')
        print('这是test02()方法...')

    def test03(self):
        # print('方法要开始执行了...')
        print('这是test03()方法...')


if __name__ == "__main__":
    # Test01().test01()
    # Test01().test02()
    # t = Test01()
    # t.test01()
    # t.test02()
    # t.test03()
    unittest.main()
