from selenium import webdriver

web_site = "http://192.168.99.100:5000/"
driver = webdriver.Chrome(executable_path="chromedriver.exe")
# default timeout of 10 sec
driver.implicitly_wait(10)
# open website
driver.get(web_site)
print(driver.find_element_by_xpath('//body[contains(text(), "I have been seen")]').text)
driver.quit()

