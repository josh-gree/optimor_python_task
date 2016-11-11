from utils import initialise_browser, get_country_data, get_table_data
from time import sleep

# hard code list of countries for now - could read from file or take CL args?
countries = 'Canada, Germany, Iceland, Pakistan, Singapore, South Africa'
countries = countries.split(',')
countries = [country.strip() for country in countries]

try:
    browser = initialise_browser()
except Exception as e:
    print("Not able to initialise browser object - {}".format(e))

browser.get('http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk')

# possibly not the best test since title my change but if this does happen may mean format
# of whole page has changed...so good to know!
assert browser.title == 'O2 | International | International Caller Bolt On'

# locate search box
search_box = browser.find_element_by_id('countryName')

# conduct country queries
for country in countries:

    data_monthly = get_country_data(browser,country)
    data_go = get_country_data(browser,country,'payandgoTariffPlan')

    print(data_monthly)

    print(data_go)



browser.close()
