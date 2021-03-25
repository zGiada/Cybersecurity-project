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
            driver.get(link+"&sk=about_contact_and_basic_info")            
        else :
            driver.get(link+"/about_contact_and_basic_info")
        time.sleep(2)
        try:                     
                prova = driver.find_element_by_xpath("//div[@class='dati1w0a tu1s4ah4 f7vcsfb0 discj3wi']").text
                #stampa tutto
                time.sleep(5)
                with open('copy.txt', 'w') as wf:
                    txt = (prova +"\n\n--------------------------")
                    wf.write(txt + '\n')
                    wf.close()
                
                regexp = re.compile(r"\d{4}")

                find = False                
                file = open('copy.txt', 'r')
                for line in file.readlines():
                    if regexp.search(line):
                        year = line
                        find = True
                file.close()            
                os.remove("copy.txt")
                
                with open('age/age.txt', 'a') as wf:
                    if find:
                        convert = int(year)
                        #print(type(convert))
                        eta_plus = 2021-convert
                        age_plus = str(eta_plus)
                        eta = eta_plus-1
                        age = str(eta)
                        txt = ("\nURL profilo: "+link+"\nAnno di nascita: "+year+"Età: "+age+"/"+age_plus+"\n--------------------------")
                        if eta_plus <= 18:
                            with open("class_18.txt", "a") as cl :
                                testo = ("URL profilo: " + link+"\n")
                                cl.write(testo)
                                cl.close()
                        if eta_plus > 18 and eta_plus < 50:
                            with open("class_18_x_50.txt", "a") as cl :
                                testo = ("URL profilo: " + link+"\n")
                                cl.write(testo)
                                cl.close()     
                        if eta_plus >= 50:
                            with open("class_50.txt", "a") as cl :
                                testo = ("URL profilo: " + link+"\n")
                                cl.write(testo)
                                cl.close()                     
                    else :
                        txt = ("\nURL profilo: "+link+"\nAnno di nascita: non presente\n--------------------------")
                        with open("class_nascosta.txt", "a") as cl :
                            testo = ("URL profilo: " + link+"\n")
                            cl.write(testo)
                            cl.close()     
                    wf.write(txt + '\n')
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






