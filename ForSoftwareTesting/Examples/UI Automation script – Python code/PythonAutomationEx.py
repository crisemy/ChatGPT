from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Specify the path to the chromedriver executable
# chromedriver_path = 'path/to/chromedriver'
chromedriver_path = '/usr/local/bin/chromedriver'

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=chromedriver_path)

# Open the URL of the website
url = 'https://automationgig.com/'
driver.get(url)

# Wait for the "Learn More" link to be clickable
learn_more_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.LINK_TEXT, 'Learn More'))
)

# Click on the "Learn More" link
learn_more_link.click()

# Close the browser
driver.quit()
