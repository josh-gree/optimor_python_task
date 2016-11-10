from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def initialise_browser():
    '''
    This function will initialise the selenium browser object

    Input:
        None

    Output:
        browser -> selenium browser object
    '''
    path_to_chromedriver = './chromedriver'
    browser = webdriver.Chrome(path_to_chromedriver)
    return browser
