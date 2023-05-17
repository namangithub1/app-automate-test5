import pytest
from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
import time


@pytest.fixture(scope="module")
def driver(request):

    # Initialize the remote WebDriver instance
    driver = webdriver.Remote()

    # def fin():
    #     driver.quit()

    # request.addfinalizer(fin)
    return driver

# Define passwords
@pytest.fixture(params=["correct", "incorrect"])
def search_term(request):
    deets = ["",""]
    if request.param == "correct":
        deets = ["browserstack","correct"]
    elif request.param == "incorrect":
        deets = ["dfgadfgasg","incorrect"]
    return deets

def test_android(driver,search_term):
    
    if search_term[1] == "incorrect":
        driver.close_app()
        driver.launch_app()
    # Test case for the BrowserStack sample Android app.
    # If you have uploaded your app, update the test case here.
    search_element = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia"))
    )
    search_element.click()
    search_input = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text"))
    )
    search_input.send_keys(search_term[0])
    time.sleep(5)
    search_results = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
    assert (len(search_results) > 0)
    driver.close_app()


    # search_input.send_keys("dfgdfgdffgdfg")
    # time.sleep(5)
    # search_results = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
    # assert (len(search_results) > 0)


