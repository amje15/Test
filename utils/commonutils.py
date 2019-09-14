from selenium import webdriver


username='adithya.sh@hashedin.com'
password='Hasher@123'


driver = webdriver.Chrome('/home/adithya_sh/Desktop/selenium_testing/chromedriver')

def driver_init():
    driver = webdriver.Chrome('/home/adithya_sh/Desktop/selenium_testing/chromedriver')
    return driver

##driver_ffx=webdriver.firefox('')




from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
import time





def clear_cache(driver, timeout=60):
    """Clear the cookies and cache for the ChromeDriver instance."""
    # navigate to the settings page
    driver.get('chrome://settings/clearBrowserData')
    wait = WebDriverWait(driver, timeout)
    # wait for the button to appear
    # click the button to clear the cache
    time.sleep(5)
    button=driver.find_element_by_css_selector('*/deep/#clearBrowsingDataConfirm').click()
    print(button)
    ##time.sleep(10)
    # wait for the button to be gone before returning

