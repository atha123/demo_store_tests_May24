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

#Enter the test data to register (later write a program to randomly create email ids so you dont get the "User already exists" error)
login_email=driver.find_element(By.ID,"reg_email")
login_email.send_keys(email)
login_passw=driver.find_element(By.ID,"reg_password")
login_passw.send_keys("pass1234567!@")
submit_btn=driver.find_element(By.NAME,"register")
submit_btn.click()
time.sleep(1)

link=driver.find_element(By.CSS_SELECTOR,"#post-9 > div > div > nav > ul > li.woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--dashboard.is-active > a")

# If the registration was successful, then print "Success" otherwise print "Fail!"
if link.is_displayed():
    print("Registered Successfully!!")
else:
    print("Fail! Did not go into the account!")