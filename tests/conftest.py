import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    # Setup: Initialize the WebDriver
    # Using webdriver_manager to automatically handle the driver executable
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Maximize the browser window
    driver.maximize_window()

    # Yield the driver instance to the test function
    yield driver

    # Teardown: Close the browser after the test is complete
    driver.quit()