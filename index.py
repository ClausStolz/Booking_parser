import controller as cntr
from urllib.parse import urlencode
import json
import io


parse_сontroller = cntr.Parser_сontroller()

url = "https://www.booking.com/searchresults.ru.html?ss=Vladivostok"
offset = 0

with io.open('hotels.json', 'w', encoding='utf8') as json_file:
    json_file.write("[")
    while (offset <= 500):
        hotel_list = parse_сontroller.gen_hotel_list(url + "&rows=15&offset=" + str(offset))
        offset += 15

        for i in hotel_list:
            try:
                h = parse_controller.gen_hotel("https://www.booking.com" + i)
                json_file.write(h.to_JSON())
                json_file.write(",")
            except:
                pass

    json_file.write("]")
