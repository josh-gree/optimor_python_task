import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


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


    # this is really hacky should be a better way to do this
    # but seems to work...
    try:
        data = get_table_data(browser,plan_type)
    except StaleElementReferenceException:
        data = get_table_data(browser,plan_type)

    return data

def get_table_data(browser,plan_type = 'paymonthlyTariffPlan'):
    '''
    This function will extract the data from the standardrates table on the page

    Inputs:
        browser -> selenium browser object

    Output:
        data -> mobile,landline and sms costs for current country returned as a dict
    '''
    table = WebDriverWait(browser, 4).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="{}"]//*[@id="standardRatesTable"]'.format(plan_type)))
    )
    rows =  [row.find_elements_by_xpath('.//td') for row in table.find_elements_by_xpath('.//tr')]
    row_labels = [row[0].get_attribute('innerHTML') for row in rows]
    row_values = [row[1].get_attribute('innerHTML') for row in rows]
    data = dict(zip(row_labels,row_values))

    return data

def parse_data(data):

    df = pd.DataFrame(data)

    df['country'] = df[0].str.split().map(lambda x : "_".join(x).lower())
    df['mobile_cost'] = df[1].map(lambda x : float(x['Mobiles'][1:]))
    df['landline_cost'] = df[1].map(lambda x : float(x['Landline'][1:]))
    df['txtmsg_cost'] = df[1].map(lambda x : float(x['Cost per text message'][:-1])/100)
    df = df.drop([0,1],axis=1)

    return df
