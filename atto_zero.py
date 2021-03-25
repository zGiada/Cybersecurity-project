from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import sys
import re
import os

#Funzione derivata dal prototipo n.01
def imgProfile():            
    time.sleep(3)
    #controlla se c'è una storia, perchè nel caso essa gi sia, il processo per pescare l'immagine del profilo è nettamente differente
    try:
        #clicca sulla storia
        driver.find_element_by_xpath("//div[@class='oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 q9uorilb mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh p8dawk7l oo9gr5id']").click()
        time.sleep(3)
        #viene aperto un sottomenu con due opzioni: vedere la storia o vedere l'immagine del profilo. Il tool prende il link per vedere l'immagine del profilo da "visualizza l'immagine del profilo"
        select_img = driver.find_element_by_xpath("//a[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 j83agx80 p7hjln8o kvgmc6g5 oi9244e8 oygrvhab h676nmdw cxgpxx05 dflh9lhu sj5x9vvc scb9dxdr i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l bp9cbjyn dwo3fsh8 btwxx1t3 pfnyh3mw du4w35lb'][last()]").get_attribute('href')     
        #va al link dell'immagine
        driver.get(select_img)
        try:
            time.sleep(3)
            #prende l'alt dell'immagine
            img_alt = driver.find_element_by_xpath("//div[@class='bp9cbjyn j83agx80 cbu4d94t taijpn5t l9j0dhe7']//img").get_attribute('alt')                
            #prende il link dell'immagine
            img_src = driver.find_element_by_xpath("//div[@class='bp9cbjyn j83agx80 cbu4d94t taijpn5t l9j0dhe7']//img").get_attribute('src')    
            #salvo in un file i dati raccolti
            with open("img_profile.txt", "a") as wf:
                txt = ("\nURL profilo: " + link + "\nALT immagine profilo: " + img_alt + "\nURL immagine profilo: " + img_src +"\n\n--------------------------")
                wf.write(txt + '\n')
                wf.close()
        except Exception as error:
            print(error)        
            driver.quit()  
    except NoSuchElementException:
        try:
            #clicca sull'immagine di profilo
            driver.find_element_by_xpath("//a[@class='oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 q9uorilb mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh p8dawk7l oo9gr5id']").click() 
            try:
                time.sleep(3)
                #prende l'alt dell'immagine
                img_alt = driver.find_element_by_xpath("//div[@class='bp9cbjyn j83agx80 cbu4d94t taijpn5t l9j0dhe7']//img").get_attribute('alt')   
                #prende il link dell'immagine             
                img_src = driver.find_element_by_xpath("//div[@class='bp9cbjyn j83agx80 cbu4d94t taijpn5t l9j0dhe7']//img").get_attribute('src') 
                #salvo nel file corretto i dati raccolti
                with open("img_profile.txt", "a") as wf:
                    txt = ("\nURL profilo: " + link + "\nALT immagine profilo: " + img_alt + "\nURL immagine profilo: " + img_src +"\n\n--------------------------")
                    wf.write(txt + '\n')
                    wf.close()  
            except Exception as error:
                print(error)
                driver.quit()
        except Exception as error:
            print(error)
            driver.quit()

#Funzione derivata dal prototipo n.02
def ageProfile(): 
    time.sleep(3) 
    try:                  
        #cattura il contenuto testuale del div riferito, dove si trovano i dati personali, tra cui l'anno di nascita
        capture = driver.find_element_by_xpath("//div[@class='dati1w0a tu1s4ah4 f7vcsfb0 discj3wi']").text
        time.sleep(3)
        #salvo i dati raccolti in un file temporaneo
        with open('copy.txt', 'w') as wf:
            txt = (capture +"\n\n--------------------------")
            wf.write(txt + '\n')
            wf.close()
        #dichiaro un'espressione regolare che ricerca espressioni di di 4 cifre                  
        regexp = re.compile(r"\d{4}")
        find = False                
        #apro il file temporaneo
        file = open('copy.txt', 'r')
        #controllo per ogni riga il contenuto
        for line in file.readlines():
            #confronto il contenuto della riga con l'espressione regolare
            if regexp.search(line):
                year = line
                find = True
        file.close()            
        #elimino il file temporaneo
        os.remove("copy.txt")      
        #salvo nel file corretto i dati raccolti   
        with open('age.txt', 'a') as wf:
            if find:
                convert = int(year)
                eta_plus = 2021-convert
                age_plus = str(eta_plus)
                eta = eta_plus-1
                age = str(eta)
                txt = ("\nURL profilo: "+link+"\nAnno di nascita: "+year+"Età: "+age+"/"+age_plus+"\n--------------------------")                 
            else :
                txt = ("\nURL profilo: "+link+"\nAnno di nascita: non presente\n\n--------------------------") 
            wf.write(txt + '\n')
            wf.close()                  
    except Exception as error:
        print(error)
        driver.quit()

#Funzione derivata dal prototipo n.03
def selectCity():
    time.sleep(3) 
    try:                                  
        #cattura il contenuto testuale del div riferito, dove si trovano i dati personali, tra cui la città di residenza
        capture = driver.find_element_by_xpath("//div[@class='dati1w0a tu1s4ah4 f7vcsfb0 discj3wi']").text
        time.sleep(3)     
        #salvo i dati raccolti in un file temporaneo
        with open('copy.txt', 'w') as wf:
            txt = (capture +"\n\n--------------------------")
            wf.write(txt + '\n')
            wf.close()        
        find = False
        #apro il file temporaneo
        file = open('copy.txt', 'r')
        #controllo per ogni riga il contenuto
        for line in file.readlines():
            #confronto il contenuto della riga con la stringa "Vive a", inizio della stringa dove viene visualizzata, se presente, la città di residenza
            if "Vive a" in line:
                city = line
                find = True            
        file.close()       
        #elimino il file temporaneo     
        os.remove("copy.txt")
        #salvo nel file corretto i dati raccolti  
        with open('city.txt', 'a') as wf:
            if find:
                txt = ("\nURL profilo: "+link+"\nResidenza: "+city+"\n--------------------------")                    
            else :
                txt = ("\nURL profilo: "+link+"\nResidenza: non presente\n--------------------------")                    
            wf.write(txt + '\n')
            wf.close()         
    except Exception as error:
        print(error)
        driver.quit()

#Funzione derivata dal prototipo n.04
def selectOccupation():
    time.sleep(3)
    try:                     
        #cattura il contenuto testuale del div riferito, dove si trovano i dati personali, tra cui il lavoro e l'università
        capture = driver.find_element_by_xpath("//div[@class='dati1w0a tu1s4ah4 f7vcsfb0 discj3wi']").text
        #salvo i dati raccolti in un file temporaneo
        with open('copy.txt', 'w') as wf:
            txt = (capture +"\n\n--------------------------")
            wf.write(txt + '\n')
            wf.close()        
        lavoro_bool = False
        uni_bool = False                                    
        #apro il file temporaneo
        file = open('copy.txt', 'r')   
        #controllo per ogni riga il contenuto         
        for line in file.readlines():   
            #confronto il contenuto della riga con la stringa "Lavor", inizio della stringa dove viene visualizzato, se presente, il lavoro
            if "Lavor" in line:        
                lavoro = line                    
                lavoro_bool = True          
            #confronto il contenuto della riga con la stringa "Università", inizio della stringa dove viene visualizzata, se presente, l'università'                    
            if "Università" in line:                    
                uni = line                    
                uni_bool = True                                                             
        file.close()
        #elimino il file temporaneo    
        os.remove("copy.txt")

        #se il lavoro non è stato identificato, si deve controllare anche un'altra pagina dove, se è stato inserito, sicuramente viene visualizzato
        if lavoro_bool == False:
            if "profile.php" in link :
                driver.get(link+"&sk=about_work_and_education")            
            else :
                driver.get(link+"/about_work_and_education")
            time.sleep(3)
            #cattura il contenuto testuale del div riferito, dove si trovano i dati personali, tra cui il lavoro
            capture = driver.find_element_by_xpath("//div[@class='dati1w0a tu1s4ah4 f7vcsfb0 discj3wi']").text
            #salvo i dati raccolti in un file temporaneo
            with open('copy.txt', 'w') as wf:
                txt = (capture +"\n\n--------------------------")
                wf.write(txt + '\n')
                wf.close()            
            lineLavoro = 0              
            #apro il file temporaneo              
            file = open('copy.txt', 'r')   
            #controllo per ogni riga il contenuto         
            for line in file.readlines():
                #confronto il contenuto della riga con la stringa "Lavor", inizio della stringa dove viene visualizzato, se presente, il lavoro
                if "Lavoro" in line:
                    lineLavoro = 1                    
                if lineLavoro == 2 :
                    lavoro = line                    
                    lavoro_bool = True                          
                lineLavoro = lineLavoro+1            
            file.close()    
            #elimino il file temporaneo    
            os.remove("copy.txt")                           
            #salvo nel file corretto i dati raccolti  
            with open('occupation.txt', 'a') as wf:
                if lavoro_bool:
                    txtLavoro = ("Lavoro: "+lavoro)                    
                else :
                    txtLavoro = ("Lavoro: niente da mostrare")
                if uni_bool :
                    txtUni = ("Università: "+uni)                    
                else :
                    txtUni = ("Università: niente da mostrare")                                
                wf.write('\n\nURL profilo: '+link+'\n\n'+txtLavoro+'\n'+txtUni+'\n\n--------------------------')
                wf.close()         
            driver.quit()                                                   
    except Exception as error:
        print(error)
        driver.quit()

# -------------- MAIN -------------- #
#controllo che il numero di parametri inseriti sia corretto
if len(sys.argv) != 4: #nome_script, email, password, linkprofilo
   print("incorrect number of parameters entered")
   sys.exit()
#assegno ogni parametro ad una variabile
nome_script, email, password, link = sys.argv

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#vado alla pagina del login di Facebook
driver.get('https://www.facebook.com')
time.sleep(3)

#Chiusura dei cookies
try: 
    driver.find_element_by_xpath("//button[@class='_42ft _4jy0 _9o-t _4jy3 _4jy1 selected _51sy']").click()
except NoSuchElementException:
    print("no cookie")

#e-mail inserita
time.sleep(3)
txtUsername = driver.find_element_by_id('email')
txtUsername.send_keys(email)
#password inserita
txtPasswd = driver.find_element_by_id('pass')
txtPasswd.send_keys(password)
time.sleep(3)

try:
    #clicco sul bottone per fare il login
    driver.find_element_by_xpath("//button[@class='_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy']").click()
    time.sleep(3)    
    #va nel profilo indicato
    try:
        driver.get(link)
        time.sleep(3)
        #esecuzione prototipo n.01
        imgProfile()
        #fine esecuzione prototipo n.01
        # ------------------------------------------

        #controllo tipo di link
        if "profile.php" in link :
            link_age = link+"&sk=about_contact_and_basic_info"            
        else:
            link_age = link+"/about_contact_and_basic_info"

        #mi sposto nel link corretto
        driver.get(link_age)        
        #esecuzione prototipo n.02
        ageProfile()
        #fine esecuzione prototipo n.02
        # ------------------------------------------

        #controllo tipo di link
        if "profile.php" in link :
            link_city = link+"&sk=about"
        else :
            link_city = link+"/about"
        #mi sposto nel link corretto
        driver.get(link_city)
        #esecuzione prototipo n.03
        selectCity()     
        #fine esecuzione prototipo n.03
        # ------------------------------------------   
        
        #controllo tipo di link
        if "profile.php" in link :
            link_occupation = link+"&sk=about"
        else :
            link_occupation = link+"/about"
        #mi sposto nel link corretto
        driver.get(link_occupation)
        #esecuzione prototipo n.04
        selectOccupation()        
        #fine esecuzione prototipo n.04
        # ------------------------------------------
    except Exception as error:
        print(error)
        driver.quit()
except Exception as error:
    print(error)
    driver.quit()