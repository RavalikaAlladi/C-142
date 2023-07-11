from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd

start_url = 'https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
browser = webdriver.Chrome()

browser.get(start_url)
time.sleep(10)
planets_data = []
heading = ['NAME','LIGHT-YEARS FROM EARTH','PLANET MASS','STELLAR MAGNITUDE','DISCOVERY DATE']

def scrape():
    for i in range(0,10):
        time.sleep(2)
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul",attrs=("class","exoplanet")):
            li_tags = ul_tag.find_all("li")
            temp_list =[]
            for index, li_tag in enumerate(li_tags):
                if index == 0 :
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
        planets_data.append(temp_list)
        
    browser.find_element(by=By.XPATH,value='//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]').click()

scrape()

print(planets_data)

planet_dataframe = pd.DataFrame(
    planets_data,
    columns=heading,
)
planet_dataframe.to_csv("planet_data.csv", index=True, index_label="id")
