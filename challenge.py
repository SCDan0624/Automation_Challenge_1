from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://techstepacademy.com/trial-of-the-stones')


input1_css_locator = "input[id='r1Input']"

# Assigning elements
input1_elem = browser.find_element_by_css_selector(input1_css_locator)

# Manipulate elements
input1_elem.send_keys("rock")

# locaters

###### CSS ######
# input2_css_locator = "input[id='ipt2']"

# console

# $$("input[id='ipt2']")

##### XPath ######
# button4_xpath_locator = "//button[@id='b4']"

# console

# $x("//button[@id=' b4']")
