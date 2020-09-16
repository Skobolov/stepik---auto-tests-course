from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/registration1.html")

input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']")
input1.send_keys("Ivan")
input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
input2.send_keys("Petrov")
input3 = browser.find_element_by_css_selector("[placeholder='Input your email']")
input3.send_keys("ivan@petrov")

button = browser.find_element_by_css_selector("button.btn")
button.click()

time.sleep(1)

welcome_text_elt = browser.find_element_by_tag_name("h1")
welcome_text = welcome_text_elt.text

assert "Congratulations! You have successfully registered!" == welcome_text

time.sleep(5)
browser.quit()
