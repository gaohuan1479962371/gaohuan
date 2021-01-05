from selenium import webdriver
from time import sleep

try:
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')

    # 理论上，可以利用任一属性进行定位
    # driver.find_element_by_xpath('//a[@href="http://news.baidu.com"]').click()
    # 利用多个属性进行定位
    # 多个属性之间可以用 and or not 连接进行定位
    # driver.find_element_by_xpath('//input[@class="s_ipt" and @maxlength="255"]').send_keys('JAVA')
    #不可用  # driver.find_elements_by_link_text('青岛新增9例核酸检测阳性病例').click() 
    # 文本精确定位
    # driver.find_element_by_xpath('//span[text()="青岛新增9例核酸检测阳性病例"]').click()
    # 文本模糊定位
    driver.find_element_by_xpath('//span[contains(text(),"新")]').click()
     # 不可用 # driver.find_element_by_xpath('//*[text="科比*")]').click()

except Exception as e:
    print(e)
finally:
    sleep(2)
    driver.quit()
