import controller as cntr
from urllib.parse import urlencode
import json
import io


parseController = cntr.ParserController()
# a = parseController.gen_hotel("https://www.booking.com/hotel/ru/zhiemchuzhina.ru.html")

url = "https://www.booking.com/searchresults.ru.html?ss=Vladivostok"
offset = 0
while (offset <= 500):
    hotel_list = parseController.gen_hotel_list(url + "&rows=50&offset=" + str(offset))
    offset += 50

    with io.open('hotels.json', 'w', encoding='utf8') as json_file:
        json_file.write("[")
        for i in hotel_list:
            h = parseController.gen_hotel("https://www.booking.com" + i)
            json_file.write(h.toJSON())
            json_file.write(",")
        json_file.write("]")
