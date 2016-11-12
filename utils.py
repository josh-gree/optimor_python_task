import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

from time import sleep


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


def get_country_source(browser, country):
    '''

    '''

    search_box = browser.find_element_by_id('countryName')
    search_box.clear()

    search_box.send_keys(country, Keys.ENTER)
    sleep(1)

    return browser.page_source


def get_table_data(selection):
    '''

    '''

    numerical_data = selection[1::2]

    landline_cost = float(numerical_data[0].text[1:])
    mobile_cost = float(numerical_data[1].text[1:])
    sms_cost = float(numerical_data[2].text[:-1])/100

    return (landline_cost, mobile_cost, sms_cost)
