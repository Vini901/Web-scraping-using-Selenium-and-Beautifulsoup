
from bs4 import BeautifulSoup
import requests
import driver as driver
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException,ElementNotInteractableException
import time

path='C:\Devlopment\chromedriver.exe'

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,und;q=0.8"
}

respose=requests.get("https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.55177535009766%2C%22east%22%3A-122.31488264990234%2C%22south%22%3A37.69926912019228%2C%22north%22%3A37.851235694487485%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D",headers=header)
yc_web_text=respose.text
soup=BeautifulSoup(yc_web_text, "html.parser")

class housepriceaddress:
    def __init__(self):
        self.price=[]
        self.address=[]
        self.links=[]

    def scrapingproperysite(self,soup):
        self.price.extend([pri.getText().split(" ")[0][0:6] for pri in soup.find_all(class_='list-card-price')])
        self.address.extend([add.getText() for add in soup.find_all(class_='list-card-addr')])
        for link in soup.find_all(class_='list-card-link'):
            s=link.get('href')
            if "https://www.zillow.com/" in s:
                self.links.append(s)
            else:
                self.links.append(f'https://www.zillow.com/{s}')

    def fillingdocs(self,path):
        driver=webdriver.Chrome(path)
        l=len(self.price)
        for i in range(l):
            time.sleep(1)
            driver.get('https://docs.google.com/forms/d/e/1FAIpQLSdPUY77sYxEb241JoHkR0s_eU_yz5NUpnJQwAs_hRpi9fouiQ/viewform?usp=sf_link')
            proper=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_per_month=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            webpage=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            proper.send_keys(self.address[i])
            time.sleep(1)
            price_per_month.send_keys(self.price[i])
            time.sleep(1)
            webpage.send_keys(self.links[i])
            time.sleep(1)
            submit=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
            submit.click()
            time.sleep(1)





var=housepriceaddress()
var.scrapingproperysite(soup)
var.fillingdocs(path)
print(var.price)
print(var.address)
print(var.links)