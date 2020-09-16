from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/execute_script.html")

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_id("answer")
browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
input1.send_keys(y)

input2 = browser.find_element_by_id("robotCheckbox")
input2.click()
input3 = browser.find_element_by_id("robotsRule")
input3.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(5)
browser.quit()
