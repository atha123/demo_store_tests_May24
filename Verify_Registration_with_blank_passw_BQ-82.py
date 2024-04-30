from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import string
import time

# Go to the browser and then load the site
driver=webdriver.Chrome()
driver.get("http://demostore.supersqa.com/")
driver.implicitly_wait(10)

#Find the  element - "My Account" and click it
my_account=driver.find_element(By.LINK_TEXT, "My account")
my_account.click()

#Create random email ids
letters = string.ascii_letters
length=10
result = ''.join(random.choice(letters) for _ in range(length))
email=result+"@gmail.com"
print(f"The email created is: {email}")

#Enter the test data to register. The password is blank
login_email=driver.find_element(By.ID,"reg_email")
login_email.send_keys(email)
login_passw=driver.find_element(By.ID,"reg_password")
login_passw.send_keys("")
submit_btn=driver.find_element(By.NAME,"register")
submit_btn.click()
time.sleep(1)

# Check if the actual error message matches the expected error message
# Expected error message: "Error: Please enter an account password." - Got this by doing actual_error_msg.text in terminal
expected_msg="Error: Please enter an account password."
actual_error_msg=driver.find_element(By.CSS_SELECTOR,"#content > div > div.woocommerce > ul > li")


if actual_error_msg.text == expected_msg:
    print("CORRECT MESSAGE PRINTED")
else:
    print("INCORRECT MESSAGE PRINTED")
    
