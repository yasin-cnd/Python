from lib2to3.pgen2 import driver
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()

url="https://dictionary.cambridge.org/tr/"

driver.get(url)

driver.maximize_window()  # ekran büyütülür

url="https://dictionary.cambridge.org/tr/"
driver.get(url)

searchInput=driver.find_element("name","q")



searchInput.send_keys("glass")  ##içeriğini değiştirerek aramak istediğiniz kelimeyi yazabilirsiniz


searchInput.send_keys(Keys.ENTER)  ##enter tuşuna bastırdık  from selenium.webdriver.common.keys import Keys ile
time.sleep(2)
sonucInput=driver.find_elements(By.XPATH,"//*[@id='dataset-cldt']/div[2]/div[2]/div/span/div/div[2]/div[1]/div[2]/div/div[3]/span") 
print(sonucInput[0].text)
time.sleep(1)

driver.close()