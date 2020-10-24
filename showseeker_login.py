"""
This test will determine if the login button, when pressed, opens the login page.
It will then navigate to the email and password fields and enter incorrect credentials.
Then, the test will determine if the Invalid login notification is shown to the user
The browser being accessed is Chrome.
The Chrome webdriver used is located locally. 

Classes imported
    webdriver   - for accessing the Chrome selenium webdriver
    Keys        - for accessing the selenium keys class, for keyboard press simulations
    time        - python library module for pausing the script, for visual checks and permitting
                  the page load time before enacting a successive action
    
Test Case
    1. Open Chrome and maximize the window size
    2. Enter the url "showseeker.com"
    3. Ensure the correct title "ShowSeeker" is in the page title tag
    4. Locate the "LOG IN" button using xpath "/html/body/div[4]/header/div/div[3]/nav[2]/div/a"
    5. Click on the "LOG IN" button
    6. Switch to newly opened tab
    7. Ensure new tab opens and has title of "Login | ShowSeeker"
    8. Locate email address text field using ID "email"
    9. Enter an email address into the text field
    10. Tab to the password text field using Keys.TAB
    11. Locate password text field using ID "password"
    11. Enter a password into the text field
    12. Locate the "I Agree & Login" button using ID "ssLoginBtn"
    13. Click on the "I Agree & Login" button
    14. Ensure the "Invalid username or password" notification shows using xpath
        "/html/body/form/div/div/div[1]/div[1]/div/div/div/div[2]/div"
    15. Close the browser
"""


# import selenium webdriver
from selenium import webdriver
# import selenium keys class
from selenium.webdriver.common.keys import Keys
# import selenium ActionChains class
import time

# set the url to be accessed
root_url = "https:www.showseeker.com"

# email address to be use
email_address = "bob@bob.com"

# password to be used
password_entry = "wrongPa55w3rd!"

# set the webdriver for chrome
chromeDriver = webdriver.Chrome(
    executable_path="/Users/admin/Documents/Coding/python_files/virtual_environments/virt01/drivers/chromedriver")

# maximize the window when open, wait 1sec., load the url var
chromeDriver.maximize_window()
chromeDriver.implicitly_wait(1)
chromeDriver.get(root_url)


# ensure the page name is in the title
assert "ShowSeeker" in chromeDriver.title

# set var to the element we are searching for... ID="yui_3_17_2_1_1603495020232_218"
target_element = chromeDriver.find_element_by_xpath(
    "/html/body/div[4]/header/div/div[3]/nav[2]/div/a")

# click on the target_element
target_element.click()

# wait 2 seconds for the page to properly load before the next command
time.sleep(2)

# Switch to last opened window - the Login window
chromeDriver.switch_to.window(chromeDriver.window_handles[-1])

# verify that the page title tag includes the Login page title
assert "Login | ShowSeeker" in chromeDriver.title

# pause for 2 seconds
time.sleep(2)

# locate the email text entry field
email_field = chromeDriver.find_element_by_id("email")

# click in the email field
email_field.click()

# enter email into the email field
email_field.send_keys(email_address)

# pause for 1 second
time.sleep(1)

# Tab to the password field using Keys.TAB
email_field.send_keys(Keys.TAB)

# locate the password entry field
password_field = chromeDriver.find_element_by_id("password")


# entry the password into the password field
password_field.send_keys(password_entry)

# pause for 1 second
time.sleep(1)

# locate the "I Agree and Login" button
login_button = chromeDriver.find_element_by_id("ssLoginBtn")

# click on the "I Agree and Login" button
login_button.click()

# ensure the "Invalid username or password" notification shows
try:
    chromeDriver.find_element_by_xpath(
        "/html/body/form/div/div/div[1]/div[1]/div/div/div/div[2]/div")
    print("successfully failed to login!")
except:
    print("An exception occurred")

# wait 10 seconds - simply for visual confirmation tests
time.sleep(10)

# close the focused tab
chromeDriver.close()

# switch to the other tab and close it
chromeDriver.switch_to.window(chromeDriver.window_handles[-1])
chromeDriver.close()
