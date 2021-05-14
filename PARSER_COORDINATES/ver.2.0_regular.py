# latitude - широта 55
# longitude - долгота 37

import re

name_pattern = r"<Placemark>\n{1}\s{8}<name>(.*)</name>"
coord_pattern = r"<coordinates>(.*)</coordinates>"

with open('INPUT.kml', 'r', encoding='utf-8') as kml:
    text = kml.read()
    
name_list = re.findall(name_pattern, text)
coord_list = re.findall(coord_pattern, text)

if len(name_list) == len(coord_list):
    long_list = []
    lat_list = []
    for i in range(len(coord_list)):
        tmp_list = list(coord_list[i].split(','))[:2]
        long_list.append(tmp_list[0])
        lat_list.append(tmp_list[1])
        
    print(name_list)
    print(long_list)
    print(lat_list)


# ОСТАЛОСЬ ДОБАВИТЬ ЗАПИСЬ В ФАЙЛ
    
else:
    print("Количество имен не соответствует количеству координат!")
