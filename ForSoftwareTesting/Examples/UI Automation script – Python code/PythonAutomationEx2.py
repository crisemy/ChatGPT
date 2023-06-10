from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Specify the path to the chromedriver executable
chromedriver_path = '/usr/local/bin/chromedriver'

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=chromedriver_path)

# Open the URL of the website
url = 'https://automationgig.com/'
driver.get(url)

# Wait for the "Learn More" link to be visible and clickable
wait = WebDriverWait(driver, 20)
learn_more_link = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'Learn More')))

# Scroll to the element to make it clickable
driver.execute_script("arguments[0].scrollIntoView();", learn_more_link)

# Click on the "Learn More" link
learn_more_link.click()

# Close the browser
driver.quit()