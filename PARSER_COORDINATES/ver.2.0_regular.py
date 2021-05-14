# latitude - широта 55
# longitude - долгота 37

import re

category_name_pattern = r"<Folder>\n{1}\s{6}<name>(.*)?</name>"
name_pattern = r"<Placemark>\n{1}\s{8}<name>(.*)</name>"
coord_pattern = r"<coordinates>(.*)</coordinates>"

with open('INPUT.kml', 'r', encoding='utf-8') as kml:
    text = kml.read()
    
category_list = re.findall(category_name_pattern, text)
name_list = re.findall(name_pattern, text)
coord_list = re.findall(coord_pattern, text)

if len(name_list) == len(coord_list):
    long_list = []
    lat_list = []
    for i in range(len(coord_list)):
        tmp_list = list(coord_list[i].split(','))[:2]
        long_list.append(tmp_list[0])
        lat_list.append(tmp_list[1])
        
    # debug
    # print(name_list)
    # print(long_list)
    # print(lat_list)

    output_text = ''

    for j in range(len(name_list)):
        output_text += name_list[j] + ';' + lat_list[j] + ';' + long_list[j] + '\n'

    out_file_name = 'Cat_' + category_list[0] + '.txt'

    with open(out_file_name, 'x', encoding='utf-8') as txt:
        txt.write(output_text)
    
else:
    print("Количество имен не соответствует количеству координат!")
