from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://techstepacademy.com/trial-of-the-stones')

# Riddle of Stones
stone_input = browser.find_element_by_id('r1Input')
stone_answer_butn = browser.find_element_by_css_selector(
    "button#r1Btn"
)
stone_result = browser.find_element_by_css_selector(
    "div#passwordBanner > h4"
)

# Riddle of Secrets
secret_input = browser.find_element_by_css_selector(
    "input[id='r2Input']"
)

secret_answer_butn = browser.find_element_by_css_selector(
    "button#r2Butn"
)

# Two Merchants
richest_merchant_name = browser.find_element_by_xpath(
    "//p[text()= '3000']/../span"
).text

merchant_input = browser.find_element_by_id('r3Input')
merchant_answer_butn = browser.find_element_by_css_selector(
    "button#r3Butn"
)

check_butn = browser.find_element_by_css_selector(
    "button[name='checkButn']"
)

complete_mag = browser.find_element_by_css_selector(
    "div#trialCompleteBanner h4"
)


# Run Scripts
stone_input.send_keys('rock')
stone_answer_butn.click()
password = stone_result.text

secret_input.send_keys(password)
secret_answer_butn.click()

merchant_input.send_keys(richest_merchant_name)
merchant_answer_butn.click()

check_butn.click()
assert complete_mag.text == 'Trial Complete'
