from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set the path to the ChromeDriver executable
# chrome_driver_path = 'C:\\Program Files\\Web Driver'

# Set your LinkedIn credentials
linkedin_email = 'kumarangad54706@gmail.com'
linkedin_password = 'Angad&linkedin9128'

# Set the URL of the LinkedIn profile you want to send a connection request to
profile_url = 'https://www.linkedin.com/in/angad-kumar-24522022a/'

# Initialize the Chrome driver
driver = webdriver.Chrome("C:\\Program Files\\Web Driver")

# Open the LinkedIn login page
driver.get('https://www.linkedin.com/login')

# Find the email and password input fields and enter your credentials
email_input = driver.find_element_by_id('username')
password_input = driver.find_element_by_id('password')
email_input.send_keys(linkedin_email)
password_input.send_keys(linkedin_password)

# Submit the login form
password_input.send_keys(Keys.ENTER)

# Wait for the page to load
time.sleep(3)

# Open the profile URL
driver.get('https://www.linkedin.com/in/angad-kumar-24522022a/')

# Wait for the page to load
time.sleep(3)

# Find and click the "Connect" button
connect_button = driver.find_element_by_xpath("//button[@aria-label='Connect']")
connect_button.click()

# Wait for the connection request form to appear
time.sleep(3)

# Find and click the "Send now" button to send the connection request
send_button = driver.find_element_by_xpath("//button[@aria-label='Send now']")
send_button.click()

# Wait for a few seconds
time.sleep(2)

# Close the browser
driver.quit()
