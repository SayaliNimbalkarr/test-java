from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to WebDriver
service = Service('C:\\Users\\Sayali Nimbalkar\\Downloads\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

try:
    # Open Google homepage
    driver.get('http://google.com')

    # Wait for search box and perform search
    search_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))
    search_box.send_keys('Selenium WebDriver' + Keys.RETURN)

    # Wait for search results to load and verify title
    WebDriverWait(driver, 10).until(EC.title_contains('Selenium WebDriver'))
    
    print("Test Passed: Page title contains 'Selenium WebDriver'.")

except Exception as e:
    print(f"Test Failed: {e}")

finally:
    driver.quit()
