from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

# Options are only available since client version 2.3.0
# If you use an older client then switch to desired_capabilities
# instead: https://github.com/appium/python-client/pull/720
options = XCUITestOptions().load_capabilities({
	"deviceName": "iPhone 14 Pro Max",
    "platformName": "ios",
    "platformVersion": "16"

})

@pytest.fixture()
def driver(request):

    # Initialize the remote WebDriver instance
    driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)

    # def fin():
    #     driver.quit()

    # request.addfinalizer(fin)
    return driver

# Initialize the remote Webdriver using BrowserStack remote URL
# and options defined above
# driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)

# Test case for the BrowserStack sample iOS app.
# If you have uploaded your app, update the test case here. 
def test_ios(driver):

    text_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Text Button"))
    )
    text_button.click()
    text_input = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Text Input"))
    )
    text_input.send_keys("hello@browserstack.com"+"\n")
    time.sleep(5)
    text_output = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Text Output"))
    )
    if text_output!=None and text_output.text=="hello@browserstack.com":
        assert True
    else:
        assert False

    # Invoke driver.quit() after the test is done to indicate that the test is completed.
    driver.quit()