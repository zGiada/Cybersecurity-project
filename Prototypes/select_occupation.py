from dateutil import parser
from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.common.exceptions import NoSuchElementException
import time
import sys
import re
import os

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
    driver.find_element_by_xpath("//button[@class='_42ft _4jy0 _9o-t _4jy3 _4jy1 selected _51sy']").click()
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
    time.sleep(2)
    
    try:
        if "profile.php" in link :
            #print(link+"&sk=about")
            driver.get(link+"&sk=about")            
        else :
            driver.get(link+"/about")
        time.sleep(2)
        try:                     
            inizio = driver.find_element_by_xpath("//div[@class='dati1w0a tu1s4ah4 f7vcsfb0 discj3wi']").text
            with open('copy.txt', 'w') as wf:
                txt = (inizio +"\n\n--------------------------")
                wf.write(txt + '\n')
                wf.close()
            lavoro_bool = False
            uni_bool = False                                    
            file = open('copy.txt', 'r')            
            for line in file.readlines():   
                if "Lavor" in line:        
                    lavoro = line                    
                    lavoro_bool = True          
                    #print(lavoro)
                if "Università" in line:                    
                    uni = line                    
                    uni_bool = True          
                    #print(uni)                                             
            file.close()
            os.remove("copy.txt")
            
            if lavoro_bool == False:
                if "profile.php" in link :
                    driver.get(link+"&sk=about_work_and_education")            
                else :
                    driver.get(link+"/about_work_and_education")
                time.sleep(2)
                work_education = driver.find_element_by_xpath("//div[@class='dati1w0a tu1s4ah4 f7vcsfb0 discj3wi']").text
                with open('copy.txt', 'w') as wf:
                    txt = (work_education +"\n\n--------------------------")
                    wf.write(txt + '\n')
                    wf.close()
                lineLavoro = 0                
                file = open('copy.txt', 'r')            
                for line in file.readlines():
                    #print("giroLav")
                    if "Lavoro" in line:
                        lineLavoro = 1
                            #print(line)
                    if lineLavoro == 2 :
                        lavoro = line                    
                        lavoro_bool = True                                                       
                            #print(lavoro)
                    lineLavoro = lineLavoro+1            
                file.close()    
                os.remove("copy.txt")                           


            with open('occupation.txt', 'a') as wf:
                if lavoro_bool:
                    txtLavoro = ("Lavoro: "+lavoro)                    
                else :
                    txtLavoro = ("Lavoro: niente da mostrare")

                if uni_bool :
                    txtUni = ("Università: "+uni)                    
                else :
                    txtUni = ("Università: niente da mostrare")

                wf.write('\n\nURL profilo: '+link+'\n\n'+txtLavoro+'\n'+txtUni+'\n\n------------------------------------------------------------------')
                wf.close()         
            
            driver.quit()                       
                            
        except:
            print("information not found")
            driver.quit()
    except:
        print("Wrong email and/or password and or link")
        driver.quit()
except:
    print("No clicked")
    driver.quit()






