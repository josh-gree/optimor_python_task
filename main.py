from utils import initialise_browser

try:
    browser = initialise_browser()
except Exception as e:
    print("Not able to initialise browser object - {}".format(e))

browser.get('http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk')

# possibly not the best test since title my change but if this does happen may mean format
# of whole page has changed...so good to know!
assert browser.title == 'O2 | International | International Caller Bolt On'
