# Task

##Optimor Python Developer Interview Task

###Background:
A common task we perform is updating our knowledge­base of networks’ international calling costs (the cost per minute of calling a foreign country from the UK). These costs are typically based on country zones, although a list of zones and constituent countries is not always directly available, so we may have to query the network’s website directly to obtain these results.

###Task:
Install and use  Selenium (1) (or another web crawling library for Python, if you feel another is more suitable) to scrape the foll owing URL (2) for the price of calling a landline in the countr ies listed in (3) from an O2 Pay Monthly contract. Print the answers. We’re looking for good, readable Pythonic code, not just a hacked­together script.
1. http://selenium­python.readthedocs.io/
2. http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk
3. Canada, Germany, Iceland, Pakistan, Singapore, South Africa

###Tips:
 - We don’t expect you to have experience with Selenium or other web crawlers beforehand – working at Optimor involves being able to rapidly pick up tools/libraries without formal training. This task is designed to test that.
 - We expect you to make full use of the internet and available documentation.
 - We don’t recommend researching the minutiae of XPath beforehand: you should be able to consult
online documentation  during the project itself.
 - We think the task should take 1­1.5 hours, including installing and learning Selenium.
 - The countries are actually stored in a JSON file. Loading and parsing this would be a better real­life
solution, but in the context of this task, imagine this doesn’t exist ;)
 - If you enjoyed the task, you may be interested in brownie points for:
   - Good use of version control (git/hg)
      - We’d love to see lots of small commits and see your process. We don’t mind if you show the sausage-­making.
   - solid resilience and reporting for errors
   - unit testing
