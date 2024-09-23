import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

import tests.test_read as classRead


class TestUpdate:
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

        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='বুকমার্ক').click()

        bookmarks = self.driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.widget.ImageView')
        assert(len(bookmarks) == 1)

        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='হোম').click()

        classRead.TestRead().test_articleHighlight(self.driver)

        self.articleTitle = self.driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.widget.TextView')[1].get_attribute('text')


    def teardown_method(self, method):
        self.driver.quit()


    def test_bookmarkArticle(self, driver = None):
        if driver != None:
            self.driver = driver

        buttons = self.driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.widget.Button')

        buttons[2].click()

        buttons[0].click()

        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='বুকমার্ক').click()

        bookmarkTitle = self.driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.widget.ImageView')[1].get_attribute('content-desc')

        if driver == None:
            assert(self.articleTitle == bookmarkTitle)
