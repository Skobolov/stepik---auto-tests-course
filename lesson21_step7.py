from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")

z_element = browser.find_element_by_id("treasure")
x_element = z_element.get_attribute("valuex")
x = x_element
y = calc(x)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)
input2 = browser.find_element_by_id("robotCheckbox")
input2.click()
input3 = browser.find_element_by_id("robotsRule")
input3.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(5)
browser.quit()