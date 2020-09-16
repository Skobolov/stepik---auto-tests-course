from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/find_link_text")
link = str(math.ceil(math.pow(math.pi, math.e)*10000))
input7 = browser.find_element_by_link_text(link)
input7.click()
input1 = browser.find_element_by_name("first_name")
input1.send_keys("Ivan")
input2 = browser.find_element_by_name("last_name")
input2.send_keys("Petrov")
input4 = browser.find_element_by_id("country")
input4.send_keys("Russia")





time.sleep(15)
browser.quit()

