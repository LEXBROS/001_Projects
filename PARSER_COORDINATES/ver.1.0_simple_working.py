#открываем KML файл
#считываем содержимое в переменную
#убираем все пробелы
with open('INPUT.kml', 'r', encoding='utf-8') as kml:
    text = kml.read()
    text = text.replace(' ', '')
    
#создаем из исходного текста список
input_list = text.split('\n')
#объявляем пустой список для записи результата
result_list = []
category_name = ''
find_name_flag = False

#побежали по исходному списку
for ind, i in enumerate(input_list):
    if '<name>' in i and input_list[ind - 1] == '<Folder>' and find_name_flag == False: #ищем название категории/файла
        category_name = i
        category_name = category_name.replace('<name>', '')
        category_name = category_name.replace('</name>', '')
        find_name_flag = True
    if '<name>' in i and input_list[ind - 1] != '<Folder>':  #ищем имя метки
        name = i
        name = name.replace('<name>', '')
        name = name.replace('</name>', '')
        result_list.append(name)
    if '<coordinates>' in i:                                #ищем координаты метки
        coordinates = i
        coordinates = coordinates.replace('<coordinates>', '')
        coordinates = coordinates.replace('</coordinates>', '')
        result_list = result_list + coordinates.split(',')[0:2]


output_file = 'Cat_' + category_name + '_WGS_84' + '.txt'   #формируем название выходного файла

#нормализация выходных данных
output_text = ''
for j in range(0, len(result_list) - 1, 3):
    output_text += result_list[j] + ';' + result_list[j + 2] + ';' + result_list[j + 1] + '\n'

#запись результата в файл
try:
    with open(output_file, 'x', encoding='utf-8') as res:
        res.write(output_text)
    print('Файл записан! OK!')
except FileExistsError:
    print('Файл с таким именем существует. Удалите старый файл и попробуйте снова.')
