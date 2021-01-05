from selenium import webdriver
from time import sleep
import time
from selenium.webdriver.support.select import Select
import random

'''ranzhi项目'''
try:
    start = time.time()
    driver = webdriver.Chrome()
    driver.get('http://localhost/ranzhi/www/')
    driver.maximize_window()
    # 隐式等待
    # 优点
    # 节省时间
    # 写一次就好
    # 缺点
    # 有时候无效
    # 隐式等待其实等待得是整个浏览器对象(等待整个页面加载完毕)
    driver.implicitly_wait(10)
    # 登陆
    driver.find_element_by_id('account').send_keys('admin')
    driver.find_element_by_id('password').send_keys('123456')
    driver.find_element_by_id('submit').click()

    # 点击文档 'D'
    driver.find_element_by_id('s-menu-4').click()

    # 进入iframe
    iframe = driver.find_element_by_id('iframe-4')
    driver.switch_to.frame(iframe)

    # 点击创建文档库
    driver.find_element_by_id('createButton').click()

    # 选择文档库类型
    element = driver.find_element_by_id('libType')
    types = Select(element)
    types.select_by_value('custom')

    # 文档库名称
    driver.find_element_by_id('name').send_keys('Python')
    # 授权用户
    driver.find_element_by_xpath('//*[@id="users_chosen"]/ul').click()
    driver.find_element_by_xpath('//*[@id="users_chosen"]/div/ul/li[1]').click()
    # 授权分组
    driver.find_element_by_id('groups1').click()
    driver.find_element_by_id('groups2').click()
    driver.find_element_by_id('groups3').click()
    driver.find_element_by_id('groups4').click()
    driver.find_element_by_id('groups5').click()

    # 保存
    driver.find_element_by_id('submit').click()

    # 点击 维护分类
    driver.find_element_by_link_text('维护分类').click()

    # 类目
    driver.find_element_by_name('children[1]').send_keys('爬虫')
    driver.find_element_by_name('children[2]').send_keys('自动化')
    driver.find_element_by_name('children[3]').send_keys('人工智能')
    driver.find_element_by_id('submit').click()
    driver.back()
    sleep(1)

    # 进入iframe
    iframe = driver.find_element_by_id('iframe-4')
    driver.switch_to.frame(iframe)

    # 点击 创建文档
    driver.find_element_by_xpath('//*[@id="menuActions"]/a').click()

    # 分类
    element = driver.find_element_by_id('module')
    modules = Select(element)
    modules.select_by_visible_text('/自动化')

    # 授权用户
    driver.find_element_by_xpath('//*[@id="users_chosen"]/ul').click()
    driver.find_element_by_xpath('//*[@id="users_chosen"]/div/ul/li[1]').click()
    # 授权分组
    driver.find_element_by_id('groups1').click()
    driver.find_element_by_id('groups2').click()
    driver.find_element_by_id('groups3').click()

    # 文档类型
    types = ['typetext', 'typeurl']
    doctype = types[random.randint(0, 1)]
    # doctype = types[1]
    driver.find_element_by_id(doctype).click()
    # 文档标题
    driver.find_element_by_id('title').send_keys('测试文档')

    if doctype == 'typetext':
        # 文档正文
        iframe = driver.find_element_by_id('ueditor_0')
        driver.switch_to.frame(iframe)
        driver.find_element_by_xpath('/html/body').send_keys('Python自动测试...')
        # 返回到上一级的iframe
        driver.switch_to.parent_frame()
    elif doctype == 'typeurl':
        # 文档链接
        driver.find_element_by_id('url').send_keys('https://www.baidu.com')

    # 关键字
    driver.find_element_by_id('keywords').send_keys('测试')

    # 摘要
    driver.find_element_by_id('digest').send_keys('自动化')

    # 附件
    driver.find_element_by_xpath('//*[@id="fileBox1"]/tbody/tr/td[1]/div/input').send_keys(
        r'C:\Users\HP\Desktop\h11.png')

    #  保存
    driver.find_element_by_id('submit').click()
except Exception as e:
    print(e)
finally:
    driver.close()
    end = time.time()
    print('程序运行时间：', (end - start))
