from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pdb
pdb.set_trace()


# Go to the browser and then load the site
driver=webdriver.Chrome()
driver.get("http://demostore.supersqa.com/")
driver.implicitly_wait(10)

#Find the  element - "My Account" and click it
my_account=driver.find_element(By.LINK_TEXT, "My account")
my_account.click()

    
#Enter the test data to register (later write a program to randomly create email ids so you dont get the "User already exists" error)
login_email=driver.find_element(By.ID,"reg_email")
login_email.send_keys("qwerty25@gmail.com")
login_passw=driver.find_element(By.ID,"reg_password")
login_passw.send_keys("pass1234567!@")
submit_btn=driver.find_element(By.NAME,"register")
submit_btn.click()
time.sleep(1)

dashboard=driver.find_element(By.CSS_SELECTOR,"#post-9 > div > div > nav > ul > li.woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--dashboard.is-active > a")
# If the registration was successful, then print "Success" otherwise print "Fail!"
if dashboard.is_displayed:
    print("Registered Successfully!!")
else:
    print("Fail! Did not go into the account!")


# if dashboard.text=="Dashboard":
#     print("Registered Successfully!!")
# else:
#     print("Fail! Did not go into the account!")