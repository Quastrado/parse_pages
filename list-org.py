import urllib.request
from urllib.parse import urlparse

from bs4 import BeautifulSoup


def get_data(url):
    parsed_uri = urlparse(url)
    hostname = f'{parsed_uri.scheme}://{parsed_uri.netloc}/'
    if hostname != 'https://www.list-org.com/':
        raise ValueError()
    req = urllib.request.urlopen(url)
    soup = BeautifulSoup(req, 'html.parser')
    data_dict = {
        'Руководитель:': True,
        'Дата регистрации:': True,
        'Статус:': True,
        'ИНН:': False,
        'КПП:': False,
        'ОГРН:': False
    }
    output_dict = {}
    header = soup.find('div', {'class': 'header'}).find('h1')
    output_dict['Наименование:'] = header.text
    for key in data_dict.keys():
        i = soup.find(lambda tag: tag.name=='i' and tag.text==key)
        if data_dict[key] == True:
            td = i.parent.find_next('td')
            output_dict[key] = td.text
        else:
            output_dict[key] = i.parent.find(text=True, recursive=False).strip()
    return output_dict


def display_data(data_dict):
    print('\nOutput:\n')
    for key, value in data_dict.items():
        print(f'{key} {value}')


if __name__ == '__main__':
    url = input('Enter the link to the company: ')
    try:
        data_dict = get_data(url)
        display_data(data_dict)
    except Exception as e:
        if e.code == '404' or e.reason == 'Not Found':
            exit('Page with specified URL not found')
        exit(e.reason)
    except ValueError:
        exit('The hostname of the specified URL does not match the list-org website')

# https://www.list-org.com/company/4868135