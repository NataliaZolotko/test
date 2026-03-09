import pytest
from selenium import webdriver
from data import *



@pytest.fixture(scope="function")
def driver():
    browser = webdriver.Firefox()
    
    browser.implicitly_wait(10)
    yield browser
    browser.quit()