from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common import by
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.common.exceptions import NoSuchElementException
import time
import sys

def imgProfile():            
            try:
                ########################### STORIA ###########################
                #clicca sulla storia
                driver.find_element_by_xpath("//div[@class='oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 q9uorilb mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh p8dawk7l oo9gr5id']").click()
                time.sleep(5)
                #seleziona che vuole vedere l'immagine del profilo
                select_img = driver.find_element_by_xpath("//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 oi9244e8 oygrvhab h676nmdw cxgpxx05 dflh9lhu sj5x9vvc scb9dxdr i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn dwo3fsh8 btwxx1t3 pfnyh3mw du4w35lb'][last()]").get_attribute('href')     
                driver.get(select_img)
                try:
                    time.sleep(5)
                    img_alt = driver.find_element_by_xpath("//div[@class='bp9cbjyn j83agx80 cbu4d94t taijpn5t l9j0dhe7']//img").get_attribute('alt')                
                    img_src = driver.find_element_by_xpath("//div[@class='bp9cbjyn j83agx80 cbu4d94t taijpn5t l9j0dhe7']//img").get_attribute('src')    
                    with open("img_profile.txt", "a") as wf:
                        txt = ("\nURL profilo: " + link + "\nALT immagine profilo: " + img_alt + "\nURL immagine profilo: " + img_src +"\n\n--------------------------")
                        wf.write(txt + '\n')
                        wf.close()
                    driver.quit();
                except:
                    print("alt don't take")
                driver.quit()                            
            except NoSuchElementException:
                ########################### NO-STORIA ###########################
                try:
                    #clicca sull'immagine di profilo
                    driver.find_element_by_xpath("//a[@class='oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 q9uorilb mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh p8dawk7l oo9gr5id']").click() 
                    try:
                        time.sleep(2)
                        img_alt = driver.find_element_by_xpath("//div[@class='bp9cbjyn j83agx80 cbu4d94t taijpn5t l9j0dhe7']//img").get_attribute('alt')                
                        img_src = driver.find_element_by_xpath("//div[@class='bp9cbjyn j83agx80 cbu4d94t taijpn5t l9j0dhe7']//img").get_attribute('src') 
                        
                        if "person" in img_alt:
                            with open("img_profilo/reale.txt", "a") as cl :
                                testo = ("URL profilo: " + link+"\n")
                                cl.write(testo)
                                cl.close()
                        else :
                            with open("img_profilo/non_reale.txt", "a") as cl :
                                testo = ("URL profilo: " + link+"\n")
                                cl.write(testo)
                                cl.close()    

                        with open("img_profilo/list_img_profile.txt", "a") as wf:
                            txt = ("\nURL profilo: " + link + "\nALT immagine profilo: " + img_alt + "\nURL immagine profilo: " + img_src +"\n\n--------------------------")
                            wf.write(txt + '\n')
                            wf.close()                        
                        driver.quit();
                    except:
                        print("alt don't take")
                    driver.quit()               
                except:
                    print("img not take")
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
    
    #go to the profile page to add
    try:
        driver.get(link)
        time.sleep(2)
        #save IMG PROFILE        
        select = imgProfile()
    except:
        print("Incorrect link")
        driver.quit()
except:
    print("Wrong email and/or password and or link")
    driver.quit()