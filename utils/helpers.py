from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(driver, by, value, timeout=20):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

def click_element(driver, by, value):
    el = wait_for_element(driver, by, value)
    el.click()
    return el

def send_keys(driver, by, value, keys):
    el = wait_for_element(driver, by, value)
    el.send_keys(keys)
    return el
