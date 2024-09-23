import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy



class TestCreate:
    def setup_method(self, method):
        desired_cap = {"platformName": "Android",
                       "appium:platformVersion": "14",
                       "appium:deviceName": "34041JEHN24431",
                       "appium:app": "G:/LIFE-NOW/2. JOB/4Beats/q2-mobile/app/Ittefaq.apk",
                       "appium:automationName": "UiAutomator2"
                       }

        # webdriver.Remote("http://127.0.0.1:4723/", desired_cap)
        appium_options = UiAutomator2Options().load_capabilities(desired_cap)

        self.driver = webdriver.Remote("http://127.0.0.1:4723", options=appium_options)
        self.driver.implicitly_wait(15)


    def teardown_method(self, method):
        self.driver.quit()


    def test_searchBar(self, driver = None):
        if driver != None:
            self.driver = driver

        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='খুঁজুন').click()

        searchValues = self.driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.widget.ScrollView')
        assert(searchValues == [])

        self.driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.EditText').click()
        self.driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.EditText').send_keys('Sports')
        self.driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.Button').click()

        searchValues = self.driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.widget.ScrollView')
        assert(searchValues != [])
        searchValues = self.driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.view.View')
        assert(searchValues != [])


