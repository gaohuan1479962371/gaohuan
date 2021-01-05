from selenium import webdriver
from time import sleep

try:
    driver = webdriver.Chrome()
    driver.get('http://localhost/ranzhi/www')
    driver.maximize_window()
    driver.implicitly_wait(10)

    # 登录
    driver.find_element_by_id('account').send_keys('tom')
    driver.find_element_by_id('password').send_keys('123456')
    driver.find_element_by_id('submit').click()

    # 获取真实姓名
    element = driver.find_element_by_xpath('//*[@id="mainNavbar"]/div/ul[1]/li/a')
    realname = element.text
    print(realname)
    # 判断登录是否成功
    # if realname == 'Tom Crouse':
    #     print('登陆成功')
    # else:
    #     print('登陆失败')

    # 断言
    # 如果断言成功，程序继续运行；如果断言失败，程序会触发异常
    assert realname =='Tom Crouse'
    print('用例运行结束！')

    # 获取登录成功以后的title
    title = driver.title
    print(title)
    assert title == '然之协同'

    # 获取登录成功以后的url
    url = driver.current_url
    print(url)
    assert url == 'http://localhost/ranzhi/www/sys/index.html'
    print('登陆成功！')

    




finally:
    sleep(2)
    driver.close()