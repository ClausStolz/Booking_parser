import urllib3
from bs4 import BeautifulSoup
import Model.apartment

class ParserController:

    def __init__(self):
        self.Url = ""
        self.Http = urllib3.PoolManager()


    def get_url(aUrl):
        self.Url = aUrl


    def gen_hotel(aHttp):
        req = Http.request('GET', Url)
        Soup = __gen_soup(req.data.decode('utf-8'))
        HotelInfo = __gen_hotel_info(Soup)

        return Hotel(
            __gen_hotel_name(HotelInfo),
            __gen_hotel_adress(HotelInfo),
            __gen_hotel_description(HotelInfo),
            __gen_services(HotelInfo),
            __gen_hotel_apartaments(HotelInfo)
        )


    def __gen_soup(aSiteText):
        return BeautifulSoup(aSiteText, 'html.parser')


    def __gen_hotel_info(aSoup):
        return aSoup.find(
                    'div',
                    attrs={"class": "rlt-right"})


    def __gen_hotel_name(aHotelInfo):
        return aHotelInfo.find(
            'div',
            attrs={"class": "hp__hotel-title"}).find('h2').text.replace("\n", "")

    def __gen_hotel_adress(aHotelInfo):
        return aHotelInfo.find(
            'span',
            attrs={"class": " hp_address_subtitle js-hp_address_subtitle jq_tooltip "}).text.replace("\n","")


    def __gen_hotel_description(aHotelInfo):
        result = ""
        for i in aHotelInfo.find('div', attrs={"id": "property_description_content" }).find_all('p'):
            result += i.text

        return result


    def __gen_hotel_apartaments(aHotelInfo):
        result = []
        for i in aHotelInfo.find('table', attrs={"class": "roomstable rt_no_dates dr_rt_no_dates js-dr_rt_no_dates __big-buttons rt_lightbox_enabled roomstable-no-dates-expanded"}).find_all('tr'):
            try:
                apartamentCapacity = len(i.find_all('i', attrs={"class": "bicon bicon-occupancy"}))
                if (apartamentCapacity != 0):
                    apartamentName =i.find('div', attrs={"class": "room-info"}).find('a').text
                    apartamentBedTypes = []
                    for j in i.find_all('li'):
                        try:
                            apartamentBedTypes.append(j.text.replace("\n", ""))
                        except:
                            pass

                    result.append(
                        Apartment(
                            apartamentName,
                            apartamentCapacity,
                            apartamentBedTypes
                            )
                        )
            except:
                pass
        return result


    def __gen_services(aHotelInfo):
        result = {}
        for i in aHotelInfo.find('div', attrs={"class": "facilitiesChecklist"}).find_all('div'):
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
