import time
from bs4.dammit import html_meta
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

city_name = str(input("Insert the city name: "))

url = "http://www.google.com/search?q="+"weather "+city_name

option = Options()
option.headless = True

driver = webdriver.Chrome(
    options=option, executable_path=r"C:\Chrome\chromedriver.exe")
driver.get(url)

element = driver.find_element_by_xpath(
    '//*[@id="rso"]/div[1]')
html_content = element.get_attribute('outerHTML')

soup = BeautifulSoup(html_content, 'html.parser')
city = soup.find('div', class_='wob_loc').text
time = soup.find('div', class_='wob_dts').text
sky = soup.find('span', id='wob_dc').text
temperature_c = soup.find('span', id='wob_tm').text
temperature_f = soup.find('span', id='wob_ttm').text
rain = soup.find('span',  id='wob_pp').text
humidity = soup.find('span',  id='wob_hm').text
wind_kmh = soup.find('span',  id='wob_ws').text
wind_mph = soup.find('span',  id='wob_tws').text
print(city + ": ")
print(time + " " + sky)
print(" Temperature: " + temperature_c + "°C or " + temperature_f+"°F")
print(" Rain: " + rain)
print(" Humidity: " + humidity)
print(" Wind: " + wind_kmh + " or " + wind_mph)

driver.quit()
