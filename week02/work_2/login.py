from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get('https://shimo.im')
    time.sleep(1)
    login_btn = browser.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]/button')
    login_btn.click() 
    time.sleep(1)
    账号 = browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input')
    账号.send_keys("12345678910")
    密码 = browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input')
    密码.send_keys("test222")
    time.sleep(1)
    login_btn_2 =browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button')
    login_btn_2.click()
    cookies = browser.get_cookies() # 获取cookies
    print(cookies)

except Exception as e:
    print(e)
