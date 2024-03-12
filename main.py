from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests

# запись результата в файл
def writing_to_a_file(path, result):
    with open(path, 'a') as file:
        file.write(f"{result}\n")

def parse():
    proxies = {
        'http': 'http://proxy.omgtu:8080',
        'https': 'http://proxy.omgtu:8080'
    }

    url = 'https://omgtu.ru/general_information/the-structure/the-department-of-university.php'
    #url = 'https://pypi.org/project/bs4/'
    page = requests.get(url, proxies=proxies, verify= False)

    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4

    block = soup.find('div', class_ ="main__content" ).findAll('li') # находим  контейнер с нужным классом

    description = ''
    for data in block: # проходим циклом по содержимому контейнера
        if data.find('a'): # находим тег <p>
            description = data.find('a').text # записываем в переменную содержание тега
            print(description)

            writing_to_a_file('kafedri.txt', description) # запись результата в файл



parse()