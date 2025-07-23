from appium import webdriver
from appium.options.common.base import AppiumOptions

def create_driver():
    options = AppiumOptions()
    options.load_capabilities({
        "appium:automationName": "UiAutomator2",
        "appium:platformName": "Android",
        "appium:platformVersion": "16",
        "appium:deviceName": "emulator-5554",
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True
    })
    return webdriver.Remote("http://127.0.0.1:4723", options=options)
