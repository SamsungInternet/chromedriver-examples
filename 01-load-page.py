# Basic example of running Samsung Internet v8.x using ChromeDriver v2.36
import time
from selenium import webdriver

options = webdriver.ChromeOptions()

# NB. when v8 stable is released you can use with 'com.sec.android.app.sbrowser'
options.add_experimental_option('androidPackage', 'com.sec.android.app.sbrowser.beta')
options.add_experimental_option('androidActivity', 'com.sec.android.app.sbrowser.SBrowserMainActivity')
options.add_experimental_option('androidDeviceSocket', 'Terrace_devtools_remote')
options.add_experimental_option('androidExecName', 'Terrace')

# NB. chromedriver will need to be in your path! (Or change this to your specific path)
driver = webdriver.Chrome('chromedriver', chrome_options=options)

# Load a website
driver.get('https://www.samsung.com/uk/')

# Wait a little time to see it load
time.sleep(5)

driver.quit()
