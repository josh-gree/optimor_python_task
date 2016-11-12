# Usage
 - python 3 needed

 - Install requirements using [anaconda](https://www.continuum.io/downloads)
 ```
 conda create --name optimor_python_task --file requirements.txt
 ```

 - [chromedriver v2.25](https://chromedriver.storage.googleapis.com/2.25/chromedriver_mac64.zip) for mac is located in the root of the repo. This needs the most recent version of chrome to be installed.

 - python main.py will return the data...

 # My approach

My initial solution attempted to do all needed selections with selenium - this however lead to the occurrence of random StaleElementExceptions. The code seemed to run 90% of the time but then would sometimes fail - I think this is due to the use of Javascript to render the page. I did not have much success using selenium's implicit and explicit waits and so decided to work predominantly with the static html. I used selenium to make each country query and then used a system sleep to make sure the page was fully loaded. BeautifulSoup was then used to parse the data form the html. I converted the data into a structured data set using pandas and returned the required data from the Dataframe.

I have tried to make the code as resilient as possible - but this is tricky since the main cause of breaking would be due to a change in the structure of the page (changes in id's of DOM elements). I have used a range of assert statements in order to be informed if the page structure changes.
