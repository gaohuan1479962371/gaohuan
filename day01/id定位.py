from selenium import webdriver

# 初始化浏览器
driver = webdriver.Chrome()
# 访问百度首页
driver.get('https://www.baidu.com')

'''
id定位
'''
# 定位搜索栏
input = driver.find_element_by_id('kw')
# 向搜索栏写入搜索关键字
input.send_keys('美国大选')

# 定位“百度一下”
btn = driver.find_element_by_id("su")
# 点击“百度一下”
btn.click()

