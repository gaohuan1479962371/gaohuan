from selenium import webdriver
from time import sleep

'''xpath定位'''
try:
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    # 绝对路径
    driver.find
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[5]/div/div/form/span[1]/input').send_keys('美国大选')
    driver.find_element_by_xpath('//*[@id="su"]').click()
except Exception as e:
    print(e)
finally:
    sleep(3)
    driver.quit()
