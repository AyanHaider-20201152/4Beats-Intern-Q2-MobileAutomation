from appium import webdriver
from appium.options.android import UiAutomator2Options

desired_cap = {"platformName": "Android",
               "appium:platformVersion": "14",
               "appium:deviceName": "34041JEHN24431",
               "appium:app": "G:/LIFE-NOW/2. JOB/4Beats/q2-mobile/app/Ittefaq.apk",
               "appium:automationName": "UiAutomator2"
               }

# webdriver.Remote("http://127.0.0.1:4723/", desired_cap)
appium_options = UiAutomator2Options().load_capabilities(desired_cap)
driver = webdriver.Remote("http://127.0.0.1:4723", options=appium_options)

driver.quit()
