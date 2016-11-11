import pandas as pd

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
data_monthly = [(country,get_country_data(browser,country)) for country in countries]
data_paygo = [(country,get_country_data(browser,country,plan_type='payandgoTariffPlan')) for country in countries]

# clean up data and put into pandas
df_monthly = pd.DataFrame(data_monthly)
df_paygo = pd.DataFrame(data_paygo)

df_monthly['country'] = df_monthly[0].str.split().map(lambda x : "_".join(x).lower())
df_monthly['mobile_cost'] = df_monthly[1].map(lambda x : float(x['Mobiles'][1:]))
df_monthly['landline_cost'] = df_monthly[1].map(lambda x : float(x['Landline'][1:]))
df_monthly['txtmsg_cost'] = df_monthly[1].map(lambda x : float(x['Cost per text message'][:-1])/100)
df_monthly = df_monthly.drop([0,1],axis=1)

df_paygo['country'] = df_paygo[0].str.split().map(lambda x : "_".join(x).lower())
df_paygo['mobile_cost'] = df_paygo[1].map(lambda x : float(x['Mobiles'][1:]))
df_paygo['landline_cost'] = df_paygo[1].map(lambda x : float(x['Landline'][1:]))
df_paygo['txtmsg_cost'] = df_paygo[1].map(lambda x : float(x['Cost per text message'][:-1])/100)
df_paygo = df_paygo.drop([0,1],axis=1)

print(df_paygo)
print(df_monthly)

browser.close()
