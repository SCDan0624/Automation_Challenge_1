from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://techstepacademy.com/trial-of-the-stones')

# Riddle of Stones
input1_css_locator = "input[id='r1Input']"
button1_css_locator = "button[id='r1Btn']"

input1_elem = browser.find_element_by_css_selector(input1_css_locator)
button1_elem = browser.find_element_by_css_selector(button1_css_locator)

# Manipulate elements
input1_elem.send_keys("rock")
button1_elem.click()

# Answer
answer1_elem = browser.find_element_by_css_selector(
    "div#passwordBanner > h4"
)


# Riddle of Secrets
input2_css_locator = "input[id='r2Input']"
input2_elem = browser.find_element_by_css_selector(input2_css_locator)

answer2_button = browser.find_element_by_css_selector(
    "button#r2Butn"
)

password = answer1_elem.text
# Manipulate elements

input2_elem.send_keys(password)
answer2_button.click()


# Two Merchants

# Simple Approach

richest_merchant_name = browser.find_element_by_xpath(
    "//p[text()= '3000']/../span"
).text

merchant_input = browser.find_element_by_id('r3Input')
merchant_answer_button = browser.find_element_by_css_selector(
    "button#r3Butn"
)

check_butn = browser.find_element_by_css_selector(
    "button[name='checkButn']"
)

complete_mag = browser.find_element_by_css_selector(
    "div#trialCompleteBanner h4"
)

# Manipulate elements
merchant_input.send_keys(richest_merchant_name)
merchant_answer_button.click()

check_butn.click()
assert complete_mag.text == 'Trial Complete'
