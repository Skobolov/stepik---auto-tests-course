from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
input1 = browser.find_element_by_name("first_name")
input1.send_keys("Ivan")
input2 = browser.find_element_by_name("last_name")
input2.send_keys("Petrov")
input4 = browser.find_element_by_id("country")
input4.send_keys("Russia")
input3 = browser.find_element_by_class_name("form-control.city")
input3.send_keys("Smolensk")
button = browser.find_element_by_css_selector("button.btn")
button.click()


time.sleep(15)
browser.quit()

