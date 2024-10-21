from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to your WebDriver (e.g., ChromeDriver)
driver_path = 'C:\\Users\\Sayali Nimbalkar\\Downloads\\chromedriver-win64\\chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

try:
    # Step 1: Open Google homepage
    driver.get('http://google.com')

    # Step 2: Wait for the search box to become available
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'q'))
    )

    # Step 3: Enter search term and perform the search
    search_box.send_keys('Selenium WebDriver' + Keys.RETURN)

    # Step 4: Wait for search results to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'search'))
    )

    # Step 5: Verify that the page title contains the search term
    assert 'Selenium WebDriver' in driver.title, "Test Failed: Title does not contain search term."

    print("Test Passed: Page title is correct.")

except Exception as e:
    print(f"Test Failed: {e}")

finally:
    # Step 6: Close the browser
    driver.quit()
