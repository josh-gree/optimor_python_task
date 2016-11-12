import pandas as pd

from utils import initialise_browser, get_country_source, get_table_data
from bs4 import BeautifulSoup

# hard code list of countries for now - could read from file or take CL args?
countries = 'Canada, Germany, Iceland, Pakistan, Singapore, South Africa'
countries = countries.split(',')
countries = [country.strip() for country in countries]

try:
    browser = initialise_browser()
except Exception as e:
    print("Not able to initialise browser object - {}".format(e))

browser.get(
    'http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk'
    )

# possibly not the best test since title my change but if this does happen may
# mean format of whole page has changed...so good to know!
assert browser.title == 'O2 | International | International Caller Bolt On', \
        "incorrect page title: html may have changed"

# conduct country queries and extract page source
sources = [get_country_source(browser, country) for country in countries]

# close browser
browser.close()

# create soup objects
soups = [BeautifulSoup(source, "html.parser") for source in sources]

# check we got correct countries
flag_select = '#standardRates > p > img'
extracted_countries = [soup.select(flag_select)[0]['alt'] for soup in soups]
assert extracted_countries == countries, 'extracted source does not match \
                                            requested countries'

# get the data
paygo_select = '#payandgoTariffPlan #standardRatesTable > tbody > tr > td'
paymonth_select = '#paymonthlyTariffPlan #standardRatesTable > tbody > tr > td'

paygo_selections = [soup.select(paygo_select) for soup in soups]
paymonth_selections = [soup.select(paymonth_select) for soup in soups]

paygo_data = [(country, *get_table_data(selection)) for
              country, selection in zip(countries, paygo_selections)]

paymonth_data = [(country, *get_table_data(selection)) for
                 country, selection in zip(countries, paymonth_selections)]

# put into DataFrame
paygo_df = pd.DataFrame(paygo_data, columns=[
                        'country', 'landline_cost',
                        'mobile_cost', 'sms_cost'])

paymonth_df = pd.DataFrame(paymonth_data, columns=[
                           'country', 'landline_cost',
                           'mobile_cost', 'sms_cost'])

# return requested data
print(paymonth_df[['country', 'landline_cost']])
