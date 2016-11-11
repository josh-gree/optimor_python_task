from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

def get_country_data(browser,country,plan_type='paymonthlyTariffPlan'):
    '''
    This fuction will submit a country query to the website and then call
    a function to extract the data

    Inputs:
        browser -> selenium browser object
        country -> country to query
        plan_type -> paymonthly or paygo

    Output:
        data -> price data for country in a dict
    '''
    search_box = browser.find_element_by_id('countryName')
    search_box.clear()

    search_box.send_keys(country,Keys.ENTER)
    sleep(0.4)


    data = get_table_data(browser)

    return data

def get_table_data(browser):
    '''
    This function will extract the data from the standardrates table on the page

    Inputs:
        browser -> selenium browser object

    Output:
        data -> mobile,landline and sms costs for current country returned as a dict
    '''
    table = browser.find_element_by_xpath('//*[@id="paymonthlyTariffPlan"]//*[@id="standardRatesTable"]')

    rows =  [row.find_elements_by_xpath('.//td') for row in table.find_elements_by_xpath('.//tr')]
    row_labels = [row[0].get_attribute('innerHTML') for row in rows]
    row_values = [row[1].get_attribute('innerHTML') for row in rows]
    data = dict(zip(row_labels,row_values))

    return data
