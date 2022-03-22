from datetime import datetime
import time
import pyautogui
import random
from os.path import exists
import json
import logging
import pyperclip
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl


#czas
now = datetime.now()
teraz = str(now).replace(" ","_")+".log"

#logging
logging.basicConfig(filename=teraz, level=logging.INFO)
logging.info("starting")
logging.info(now)

#disclaimer
logging.info("I am not responsible for any consequences that using this software may bring upon you. Have fun! ;)")
print("I am not responsible for any consequences that using this software may bring upon you. Have fun! ;)")

#sprawdzenie,czy jest plik konfiguracyjny
file_exists = exists("conf.json")
if file_exists == True:
    #pobranie z niegokoordynatow
    logging.info("config openned.")
    f = open("conf.json")
    data = json.load(f)

    x_cell = data["cell"][0]
    y_cell = data["cell"][1]
    
    x_field = data["field"][0]
    y_field = data["field"][1]
    
    x_name= data["name"][0]
    y_name = data["name"][1]

    guzik = data["button"]

    #mailing
    if data["email"]==1:
        em_host = data["em_host"]
        em_user = data["em_user"]
        em_password = data["em_password"]
        em_recepient = data["em_recepient"]

    logging.info("config loaded.")
else:
    logging.error("no conf.json file!! program stops.")
    print("no conf.json file!! program stops.")
    exit()

#randomowe wartosci długość pauzy po kazdej akcji
milisek = random.choice(range(10,800))
ms = "0."+str(milisek)
pyautogui.PAUSE = int(float(ms))
logging.info("random pause1 length set at: "+ms)

#globale
base_scroll = 0
totalscroll = 0
edited = []
temat = "ExcelBot finished work."

em_plain = """
    EXCELBOT finished work. See the log file for more details.
"""

def wyslij(nad, has, odb, serw, port, suchy, mokry, temat_wiad):
    message = MIMEMultipart("alternative")
    message["Subject"] = temat_wiad
    message["From"] = nad
    message["To"] = odb
    part1 = MIMEText(suchy, "plain")
    part2 = MIMEText(mokry, "html")
    message.attach(part1)
    message.attach(part2)
    context = ssl.create_default_context()
    try:
        smtpobj = smtplib.SMTP_SSL(serw, port)#context=context, ale na windzie to nie dziala
        smtpobj.login(nad, has)
        smtpobj.sendmail(nad, odb, message.as_string())
        smtpobj.quit()
        logging.info("Mail sent successfully. End of execution.")
        print("Mail sent successfully. End of execution.")
        logging.info("****JEB4Ć*T0RUŃ****BDG_SQUAD****")
        print("****JEB4Ć*T0RUŃ****BDG_SQUAD****")
    except smtplib.SMTPException:
        logging.error("error in mail sending process!")
        print("error in mail sending process!")

#wybor drogi
wybor = input("choose your path: 1 - dots / 2 - message: --> ")
wybor = int(wybor)
print(wybor)

if wybor==1:
    #droga kropki
    logging.info("the way of the dot has been chosen")
    il = input("how many times do you want to loop: --> ")
    logging.info("ammount of loops set at: "+il)
    for x in range(0, int(il)):
        logging.info("start of loop: "+str(x+1)+"/"+str(il))
        #opoznienie po ukonczeniu petli
        opoz = random.choice(range(12, 180))
        if (x+1)/int(il)==1:
            logging.info("LAST LOOP.")
            print("LAST LOOP.")
            opoz = 3
        print(str(x+1)+"/"+il)
        if totalscroll>=120:
            rand1 = random.choice(range(1,2))
            if rand1 == 1:
                logging.info("scroll > 120 i rand choise 1 -> scrolling +5 units")
                pyautogui.scroll(5)
            if rand1 == 2:
                logging.info("scroll > 120 i rand choise 2 -> scrolling -5 units")
                pyautogui.scroll(-5)
            totalscroll=0
        if x!=0 and x%7==0:
            rand2 = random.choice(range(1,2))
            if rand2 == 1:
                logging.info("x!=0 i and can be divided by 7 i rand choice 1 -> scrolling -10 units")
                pyautogui.scroll(-10)
            if rand2 == 2:
                logging.info("x!=0 i and can be divided by 7 i rand choice 2 -> scrolling +10 units")
                pyautogui.scroll(10)
            totalscroll=0
        #randomowa wysokosc scrollu
        scrl = random.choice(range(-20,50))
        #losowy czas trwania ruszania myszką
        nr = random.choice(range(1, 3))
        pyautogui.moveTo(x_cell,y_cell, duration=nr, tween=pyautogui.easeInOutQuad)
        pyautogui.scroll(scrl)
        time.sleep(0.2)
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.moveTo(x_field, y_field, duration=nr, tween=pyautogui.easeInOutQuad)
        time.sleep(0.2)
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.write(".", interval=0.06)
        time.sleep(0.2)
        pyautogui.press("enter")
        time.sleep(0.2)
        pyautogui.moveTo(x_name,y_name, duration=nr, tween=pyautogui.easeInOutQuad)
        time.sleep(0.2)
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.hotkey(guzik, 'c')
        spot = pyperclip.paste()
        edited.append(spot)
        time.sleep(0.2)
        pyautogui.moveTo(x_cell,y_cell, duration=nr, tween=pyautogui.easeInOutQuad)
        time.sleep(0.2)
        pyautogui.click()
        time.sleep(0.2)
        #pyautogui.hotkey('command', 'z')
        totalscroll = totalscroll+scrl
        logging.info("made changes in: "+spot)
        print("made changes in: "+spot)
        print("end of loop "+str(x+1)+". delay before next action "+str(opoz))
        logging.info("end of loop "+str(x+1)+". delay before next action "+str(opoz))
        time.sleep(opoz)

if wybor==2:
    #droga wiadomosci
    print("the way of the message has been chosen.")
    il = input("how many times do you want to loop: --> ")
    tekst = input("enter your message: --> ")
    for x in range(0, int(il)):
        print("loop "+str(x+1)+"/"+il)
        if totalscroll>=120:
            rand1 = random.choice(range(1,2))
            if rand1 == 1:
                print("scrolling +20")
                pyautogui.scroll(20)
            if rand1 == 2:
                print("scrolling -20")
                pyautogui.scroll(-20)
            totalscroll=0
        if x!=0 and x%7==0:
            rand2 = random.choice(range(1,2))
            if rand2 == 1:
                print("scrolling +15")
                pyautogui.scroll(-15)
            if rand2 == 2:
                print("scrolling -15")
                pyautogui.scroll(15)
            totalscroll=0
        #randomowa wysokosc scrollu
        scrl = random.choice(range(-20,50))
        #losowy czas trwania ruszania myszką
        nr = random.choice(range(1, 3))
        pyautogui.moveTo(551,561, duration=nr, tween=pyautogui.easeInOutQuad)
        pyautogui.scroll(scrl)
        time.sleep(0.2)
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.write(tekst, interval=0.06)
        time.sleep(0.2)
        pyautogui.moveRel(30, 30)
        time.sleep(0.2)
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.hotkey('command', 'z')
        totalscroll = totalscroll+scrl

elements = [f'<li>{e}</li>' for e in edited]

tresc = "<h1>ExcelBot v.0.6.9</h1><h2>Edited theese cells:</h2><ul>"+"".join(elements)+"</ul><h3>****JEB4Ć*T0RUŃ****BDG_SQUAD****</h3>"
logging.info("sending email.")
print("sending email.")
wyslij(em_user, em_password, em_recepient, em_host, 465, em_plain, tresc, temat)