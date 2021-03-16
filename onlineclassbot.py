#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pyautogui
import webbrowser as wb
import time
from datetime import datetime
import random
pazartesi=13
sali=9
carsamba=10
carsamba2=13
persembe=9
persembe2=13
cuma=14
gün=int(input(print("Gün Seçiniz:")))
if gün==1:
    target=pazartesi
    target2=0
elif gün==2:
    target=sali
    target2=0
elif gün==3:
    target=carsamba
    target2=carsamba2
elif gün==4:
    target=persembe
    target2=persembe2
elif gün==5:
    target=cuma
    target2=0
liste=["Gunaydin Hocam.","Gunaydin","Hayirli Sabahlar.","Good Morning","Merhabalar","Selam","iyi gunler"]
kelam=random.choice(liste)
while True:
    suan=datetime.now()
    if suan.hour==target and suan.minute==10 and suan.second==0:
        wb.open("https://online.yildiz.edu.tr/Account/Login")
        time.sleep(5)
        pyautogui.click(891,499)
        pyautogui.click(891,568)
        pyautogui.press("ENTER")
        time.sleep(10)
        pyautogui.click(840,429)
        time.sleep(5)
        pyautogui.click(1447,538)
        time.sleep(3)
        pyautogui.click(1084,187)
        time.sleep(7)
        pyautogui.click(898,535)
        time.sleep(5)
        pyautogui.click(1199,409)
        time.sleep(2)
        pyautogui.click(975,1056)
        pyautogui.typewrite(kelam)
        pyautogui.press("ENTER")
        #pyautogui.click(1447,608)
    if target2 != 0:
        if suan.hour==target2 and suan.minute==36 and suan.second==0:
            wb.open("https://online.yildiz.edu.tr/Account/Login")
            time.sleep(5)
            pyautogui.click(891,499)
            pyautogui.click(891,568)
            pyautogui.press("ENTER")
            time.sleep(10)
            pyautogui.click(840,429)
            time.sleep(5)
            pyautogui.click(1447,538)
            time.sleep(3)
            pyautogui.click(1084,187)
            time.sleep(7)
            pyautogui.click(898,535)
            time.sleep(5)
            pyautogui.click(1199,409)
            time.sleep(2)
            pyautogui.click(975,1056)
            pyautogui.typewrite(kelam)
            pyautogui.press("ENTER")
            #pyautogui.click(1447,608)
            break
    
        

            


# In[ ]:




