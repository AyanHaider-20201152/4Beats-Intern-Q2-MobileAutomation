import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy



class TestRead:
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


    def test_articleHighlight(self, driver = None):
        if driver != None:
            self.driver = driver

        articles = []
        while len(articles) <2:
            articles = self.driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.widget.ImageView')
        topArticle = articles[1]
        topArticleTitle = topArticle.get_attribute('content-desc')

        topArticle.click()

        articleTitle = self.driver.find_elements(by=AppiumBy.CLASS_NAME, value='android.widget.TextView')[1].get_attribute('text')

        if driver == None:
            assert(topArticleTitle == articleTitle)


    def test_menu(self, driver = None):
        if driver != None:
            self.driver = driver

        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='মেনু').click()

        self.driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.ScrollView')
        optionTop = self.driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.ScrollView').find_element(by=AppiumBy.CLASS_NAME, value='android.view.View')
        optionTopTitle = optionTop.get_attribute('content-desc')
        optionTop.click()

        pageTitle = self.driver.find_element(by=AppiumBy.CLASS_NAME, value='android.view.View').get_attribute('content-desc')

        if driver == None:
            assert(optionTopTitle == pageTitle)



