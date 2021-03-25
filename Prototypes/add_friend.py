from selenium import webdriver
from getpass import getpass
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.common.exceptions import NoSuchElementException
import time
import sys

if len(sys.argv) != 4: #nome_script, email, password, linkprofilo
   print("incorrect number of parameters entered")
   sys.exit()

nome_script, email, password, link = sys.argv

#enter e-mail and password in the terminal
username = email
passwd = password

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#go to the facebook login page
driver.get('https://www.facebook.com')
time.sleep(2)

#close cookies
try: 
    driver.find_element_by_xpath("//button[@class='_42ft _4jy0 _9fws _4jy3 _4jy1 selected _51sy']").click()
except NoSuchElementException:
    print("no cookie")

#e-mail is entered
time.sleep(2)
txtUsername = driver.find_element_by_id('email')
txtUsername.send_keys(username)
#password is entered
txtPasswd = driver.find_element_by_id('pass')
txtPasswd.send_keys(passwd)
time.sleep(2)

#click button to login
try:
    driver.find_element_by_xpath("//button[@class='_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy']").click()
    time.sleep(5)
    
    #go to the profile page to add
    try:
        driver.get(link)
        time.sleep(5)
        #send friend request
        try:
            driver.find_element_by_xpath("//div[@class='oajrlxb2 s1i5eluu gcieejh5 bn081pho humdl8nn izx4hr6d rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys d1544ag0 qt6c0cv9 tw6a2znq i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l beltcj47 p86d2i9g aot14ch1 kzx2olss cbu4d94t taijpn5t ni8dbmo4 stjgntxs k4urcfbm tv7at329']").click() 
            time.sleep(5)
            print("friend request sent")
            driver.quit()
        except:
            print("friend request not sent")
            driver.quit()
    except:
        print("Wrong email and/or password and or link")
        driver.quit()
except:
    print("No clicked")
    driver.quit()






