import json
import wikipediaapi
from tqdm import tqdm
import datetime


def paramert_decor(path = ''):
    while True:
        path = input('''Укажите путь, по которому создать файл.
Если путь не указан, файл будет создан в директории программы.
- ''')
        if path.lower().startswith('d:\\') or path.lower().startswith('c:\\') or path == '':
            break
    file_name = input('Укажите имя файла: ')
    path += (file_name + '.json')
    def decor(function):
        def body(*args, **kwargs):
            result = function(*args, **kwargs)
            # file_name = input('Укажите имя файла: ')
            # path += (file_name + '.json')
            time_record = datetime.datetime.today().strftime('%H:%M:%S - %d.%m.%Y')
            data = {}
            data['Аргументы'] = [args, kwargs]
            data['Имя функции'] = str(function).split()[1]
            data['Значение'] = result
            data['Дата'] = time_record
            with open(path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
            print(f'Файл {file_name} создан.')

        return body
    return decor

@paramert_decor()
def dict_countries():
    with open('countries.json', encoding='utf-8') as file:
        countries = json.load(file)

    dict_conries = {}
    wiki_wiki = wikipediaapi.Wikipedia('en')

    for country in tqdm(countries, ncols=100):
        page_py = wiki_wiki.page(country['name']['common'].replace(' ', '_'))
        dict_conries[country['name']['common']] = page_py.fullurl
    return dict_conries


dict_countries()