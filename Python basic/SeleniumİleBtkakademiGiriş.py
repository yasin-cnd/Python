from lib2to3.pgen2 import driver
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

tc=""   #tc giriniz
şifre=""  #şifre giriniz
class Btk:
    def __init__(self,tc,şifre):
        self.browser=webdriver.Chrome()
        self.tc=tc
        self.şifre=şifre
      

    def sıgnIn(self) :
        self.browser.get("https://1milyonistihdam.hmb.gov.tr/ozgecmis/login?type=btk")
        time.sleep(1)
        self.browser.find_element(By.XPATH,"//*[@id='identification']").send_keys(self.tc)
        self.browser.find_element(By.XPATH,"//*[@id='password']").send_keys(self.şifre)


        self.browser.find_element(By.XPATH,"//*[@id='loginform']/button").send_keys(Keys.ENTER) 
        time.sleep(5) 
        self.browser.find_element(By.XPATH,"//*[@id='ember82']/div/div/div/a").send_keys(Keys.ENTER)
        time.sleep(10)  
        self.browser.find_element(By.XPATH,"//*[@id='__next']/div/div[1]/div[3]/div/div/div[5]/div/div").click() 
        time.sleep(7)
        self.browser.find_element(By.XPATH,"//*[@id='dropdown_profile']/ul/a[3]/li").click() 
        time.sleep(7)
        self.browser.find_element(By.XPATH,"//*[@id='main_section']/div[4]/div/div[2]/div[2]/a/p").click() #sıfırdan ileri seviye python kursu giriş
btk=Btk(tc,şifre)
btk.sıgnIn()



