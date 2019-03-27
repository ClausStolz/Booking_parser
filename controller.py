import urllib3
from bs4 import BeautifulSoup
import Model.apartment as ma
import Model.hotel as mh

class Parser_сontroller:

    def __init__(self):
        self.http = urllib3.PoolManager()


    def gen_hotel_list(self, a_url):
        soup = self.__gen_soup(a_url)
        result = self.__gen_hotel_list(soup)

        return result


    def gen_hotel(self, a_url):
        soup = self.__gen_soup(a_url)
        hotel_info = self.__gen_hotel_info(soup)

        return mh.Hotel(
            self.__gen_hotel_name(hotel_info),
            self.__gen_hotel_adress(hotel_info),
            self.__gen_hotel_description(hotel_info),
            self.__gen_services(hotel_info),
            self.__gen_hotel_apartaments(hotel_info)
        )


    def __gen_soup(self, a_url):
        req = self.http.request('GET', a_url)

        return BeautifulSoup(req.data.decode('utf-8'), 'html.parser')


    def __gen_hotel_list(self, a_soup):
        n = a_soup.find('div', attrs={"class", " nodates_hotels wider_image "})
        result = []
        for i in n.find_all('div'):
            try:
                unparsed_link = i.find('a', attrs={"class", "hotel_name_link url"})['href'].replace("\n","")
                result.append(unparsed_link.split(';')[0])
            except:
                pass

        return result


    def __gen_hotel_info(self, a_soup):
        return a_soup.find(
            'div',
            attrs={"class": "rlt-right"})


    def __gen_hotel_name(self, a_hotel_info):
        return a_hotel_info.find(
            'div',
            attrs={"class": "hp__hotel-title"}).find('h2').text.replace("\n", "")


    def __gen_hotel_adress(self, a_hotel_info):
        return a_hotel_info.find(
            'span',
            attrs={"class": " hp_address_subtitle js-hp_address_subtitle jq_tooltip "}).text.replace("\n","")


    def __gen_hotel_description(self, a_hotel_info):
        result = ""
        for i in a_hotel_info.find('div', attrs={"id": "property_description_content" }).find_all('p'):
            result += i.text

        return result


    def __gen_hotel_apartaments(self, a_hotel_info):
        result = []
        for i in a_hotel_info.find('table', attrs={"class": "roomstable rt_no_dates dr_rt_no_dates js-dr_rt_no_dates __big-buttons rt_lightbox_enabled roomstable-no-dates-expanded"}).find_all('tr'):
            try:
                apartament_capacity = len(i.find_all('i', attrs={"class": "bicon bicon-occupancy"}))
                if (apartament_capacity != 0):
                    apartament_name =i.find('div', attrs={"class": "room-info"}).find('a').text.replace("\n","")
                    apartament_bed_types = []
                    for j in i.find_all('li'):
                        try:
                            apartament_bed_types.append(j.text.replace("\n", ""))
                        except:
                            pass

                    result.append(
                        ma.Apartment(
                            apartament_name,
                            apartament_capacity,
                            apartament_bed_types
                        )
                    )
            except:
                pass

        return result


    def __gen_services(self, a_hotel_info):
        result = {}
        for i in a_hotel_info.find('div', attrs={"class": "facilitiesChecklist"}).find_all('div'):
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
            result[service_name] = service_list

        return result
