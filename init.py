# import requests
import csv
import re
import json
from bs4 import BeautifulSoup
import urllib3

http = urllib3.PoolManager()

r = http.request('GET','https://www.booking.com/hotel/ru/zhiemchuzhina.ru.html')
print(r.status)
siteText = r.data.decode('utf-8')
soup = BeautifulSoup(siteText, 'html.parser')

hotelInfo = soup.find('div', attrs={"class": "rlt-right"})

name = hotelInfo.find('div',attrs={"class": "hp__hotel-title"}).find('h2')
adress = hotelInfo.find('span',attrs={"class": " hp_address_subtitle js-hp_address_subtitle jq_tooltip "})
description = ""
for i in hotelInfo.find('div', attrs={"id": "property_description_content" }).find_all('p'):
    description += i.text

services = {}
for i in hotelInfo.find('div', attrs={"class": "facilitiesChecklist"}).find_all('div'):
    try:
        service_name = i.find('h5').text.replace("\n", "")
        service_list = []
        for j in i.find_all('li'):
            try:
                service_list.append(j.text.replace("\n", ""))
            except:
                pass
    except:
        pass
    services[service_name] = service_list


for i in hotelInfo.find('table', attrs={"class": "roomstable rt_no_dates dr_rt_no_dates js-dr_rt_no_dates __big-buttons rt_lightbox_enabled roomstable-no-dates-expanded"}).find_all('tr'):
    try:
        print(len(i.find_all('i', attrs={"class": "bicon bicon-occupancy"}))) #length
        print(i.find('div', attrs={"class": "room-info"}).find('a').text) #name
        print("\n\n\n\n")
        bed_types = []
        for j in i.find_all('li'):
            try:
                bed_types.append(j.text.replace("\n", ""))
            except:
                pass
        #bed_types
        print(bed_types)
    except:
        pass


# print(name.text.replace("\n", " "))
# print(adress.text.replace("\n", " "))
# print(description)
# print("==================")
# print(services)
