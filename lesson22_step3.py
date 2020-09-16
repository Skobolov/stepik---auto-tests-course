from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")

x_element = browser.find_element_by_id("num1")
x = x_element.text
y_element = browser.find_element_by_id("num2")
y = y_element.text

sum1 = str(int(x) + int(y))

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(sum1)

button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(15)
browser.quit()

