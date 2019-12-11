# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 20:45:55 2019

@author: Lafiz33
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from time import time
print("*"*60)
print("Auto_Browser_v1.0.2_By__Lafiz33 \nthis is a test program.. \nmax limit 102, website Blocks after that..")
print("*"*60)

url= "https://www.daraz.com.bd/"


#userInput=str(input("Enter Item Name \n\r"))
while(True):
    try:    
        page_num=int(input("how many pages you want? \n\r"))
        page_counter=1
        timer1 = []
        
        print("Creating File...")
        filename = "results.txt"
        f = open(filename, "w")
        
        
        print("Writing Headers...")
        headers= "Starting Loading Time Count For Daraz page :"
        f.write(headers+ "\n")
        
        
        print("Opening Web Browser...")
        dir_now=os.path.dirname(os.path.abspath(__file__))
        browser=webdriver.Chrome(executable_path=dir_now+'\\chromedriver.exe')
        
        while(page_counter!=page_num):
            flag = True
            for i in range(1,102) :
                start_time = time()
                browser.get(url)
                end_time = time()
                
                temp_time=round(end_time-start_time,5)
                timer1.append(float(temp_time))
                
                str1="page number :"+str(i)+" time took to load : " +str(round(end_time-start_time,5)) +"s"
                print(str1)            
                            
                print("searching for /")
                if (flag):
                    elem = browser.find_element_by_name("q")
                    elem.send_keys("/")
                    elem.send_keys(Keys.RETURN)
                    flag = False
            
            
                print("Page found..")
                print("taking notes")
                f.write(str1+"\n")
                
                if(page_counter==page_num):
                    break
                else:
                    page_counter=page_counter+1
                    print("going to next page...")
                    nextPage = browser.find_element_by_link_text(str(i+1))
                    url=nextPage.get_attribute('href')
                    print("found next page")
            if(page_counter==page_num):
                break
    #            print(timer1)
        
        time_sum = sum(timer1)
        avg = round(time_sum/page_num, 5)
        time_max = max(timer1)
        time_min = min(timer1)
        
        print("writing results..")
        f.write("total number of page :"+str(page_num)+"\n"+"minimum loading time: "+str(time_min)+" maximum loading time: "+str(time_max)+" average time: "+str(avg)+"\n")
        if(page_counter==page_num):
            break
        
    except:
        print("Something went wrong.. \nSorry.. \nTry again :(")
    finally:
        print("Closing file...")
        f.close()
        print("have fun.. :)")
        if(input("exit browser? y/n \n")=="y"):
            print("exiting..\nthank you..")
            browser.close();
            break






