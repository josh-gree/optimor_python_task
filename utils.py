import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


from time import sleep


def initialise_browser(path_to_chromedriver):
    '''
    This function will initialise the selenium browser object

    Input:
        None

    Output:
        browser -> selenium browser object
    '''
    browser = webdriver.Chrome(path_to_chromedriver)
    return browser


def get_country_source(browser, country):
    '''
    Function to query the page for a given country and then extract
    and return the source code.

    Inputs:
        browser -> selenium browser object
        country -> string representation of country to query

    Output:
        source -> html source of page as a string
    '''

    search_box = browser.find_element_by_id('countryName')
    search_box.clear()

    search_box.send_keys(country, Keys.ENTER)

    # Got to be a better way...but it works!
    sleep(1)
    source = browser.page_source

    return source


def get_table_data(selection):
    '''

    '''

    numerical_data = selection[1::2]

    landline_cost = float(numerical_data[0].text[1:])
    mobile_cost = float(numerical_data[1].text[1:])
    sms_cost = float(numerical_data[2].text[:-1])/100

    return (landline_cost, mobile_cost, sms_cost)
