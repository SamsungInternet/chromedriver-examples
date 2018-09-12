# Basic example of submitting text in Samsung Internet v8.x using ChromeDriver v2.36
import time
from selenium import webdriver

options = webdriver.ChromeOptions()

# When v8 stable is released, we can use this to access the stable version:
# options.add_experimental_option('androidPackage', 'com.sec.android.app.sbrowser')
# Using the Beta version for now:
options.add_experimental_option('androidPackage', 'com.sec.android.app.sbrowser.beta')
options.add_experimental_option('androidActivity', 'com.sec.android.app.sbrowser.SBrowserMainActivity')
options.add_experimental_option('androidDeviceSocket', 'Terrace_devtools_remote')
options.add_experimental_option('androidExecName', 'Terrace')

# NB. chromedriver will need to be in your path! (Or change this to your specific path)
driver = webdriver.Chrome('chromedriver', chrome_options=options)

# Load a website
driver.get('https://duckduckgo.com')

time.sleep(5)

# Find the search box and submit some text
search_box = driver.find_element_by_name('q')
search_box.send_keys('Samsung Internet')
search_box.submit()

time.sleep(5)

driver.quit()
