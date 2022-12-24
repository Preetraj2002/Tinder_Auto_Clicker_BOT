import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

# # # Run this in terminal to active local host (cmd prompt)
# #  #chrome.exe --remote-debugging-port=6969 --user-data-dir=C:\Users\USER\Desktop\my_python

def swiping_right(n):
    right = driver.find_element(By.XPATH,'//*[@id="q888578821"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button')

    for i in range(n):
        try:
            right.click()
        except ElementClickInterceptedException:        #Pop up appeared
            not_interested=driver.find_element(By.XPATH,'//*[@id="q-839802255"]/main/div/div[2]/button[2]')
            not_interested.click()
            time.sleep(5)
            continue
        else:
            age = driver.find_element(By.XPATH,
                                      '//*[@id="q888578821"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[2]/div[3]/div/div[1]/div/span[2]')
            print(age.text)
        finally:
            time.sleep(5)

def swiping_left(n):
    left = driver.find_element(By.XPATH,'//*[@id="q888578821"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')
    for i in range(n):
        left.click()
        time.sleep(5)



options=Options()
options.add_experimental_option("detach",True)
# options.debugger_address="localhost:6969"
options.add_argument("start-maximized")

# # driver path
chrome_driver_path="C:\\Users\\USER\\Desktop\\my_python\\chromedriver.exe"
website_URL='https://tinder.com/'

driver=webdriver.Chrome(service_log_path=chrome_driver_path,options=options)
driver.get(website_URL)
time.sleep(2)

#accept t&c
accept=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button')
accept.click()
time.sleep(2)

#click on log in
log_in = driver.find_element(By.LINK_TEXT,"Log in")
log_in.click()
time.sleep(3)

try:
    #click on fb login
    fb=driver.find_element(By.XPATH,'//*[@id="q-839802255"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
    fb.click()
    time.sleep(2)

except NoSuchElementException:
    print("ERROR")
    # click on more options
    more = driver.find_element(By.XPATH, '//*[@id="q-839802255"]/main/div/div[1]/div/div/div[3]/span/button')
    more.click()
    time.sleep(2)
    # click on fb login again
    fb = driver.find_element(By.XPATH, '//*[@id="q-839802255"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
    fb.click()
    time.sleep(2)

finally:
    # switch to new pop up window
    driver.switch_to.window(driver.window_handles[1])

    # type your id
    username = driver.find_element(By.XPATH, '//*[@id="email"]')
    username.send_keys("YOUR_EMAIL")

    # type your password
    password=driver.find_element(By.XPATH,'//*[@id="pass"]')
    password.send_keys("YOUR_PASSWORD")

    #log in
    # login=driver.find_element(By.CSS_SELECTOR,"div #buttons label #loginbutton")
    login=driver.find_element(By.NAME,"login")
    login.click()


#after loging in successfully switch back to main window
driver.switch_to.window(driver.window_handles[0])
time.sleep(10)

location=driver.find_element(By.XPATH,'//*[@id="q-839802255"]/main/div/div/div/div[3]/button[1]')
location.click()
time.sleep(5)

notify=driver.find_element(By.XPATH,'/html/body/div[2]/main/div/div/div/div[3]/button[2]')
notify.click()
time.sleep(5)

close_darkmode=driver.find_element(By.XPATH,'/html/body/div[2]/main/div/div[2]/button')
close_darkmode.click()
time.sleep(10)

swiping_right(10)


