from utils import initialise_browser
from selenium.webdriver.common.keys import Keys

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

    search_box.send_keys(country,Keys.ENTER)

    # find the paymonthlyTariffPlan table
    table = browser.find_element_by_xpath('//*[@id="paymonthlyTariffPlan"]//*[@id="standardRatesTable"]')

    print(table.get_attribute('innerHTML'))
