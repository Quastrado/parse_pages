import os
from datetime import datetime
from sys import exit
import builtins
import urllib.request
from bs4 import BeautifulSoup


def get_user_data(date_entry, resolution):
    user_date = datetime.strptime(date_entry, '%Y-%m')
    year = str(user_date.year)
    month_number = str("{:02d}".format(user_date.month - 1))
    month_name = user_date.strftime('%B').lower()
    return {'year': year,
            'month_number': month_number,
            'month_name': month_name,
            'resolution': resolution}


def file_name_generate(heading):
    file_name = 'sm_images/{heading}.png'
    if os.path.isfile(file_name):
        file_name = f'sm_images/{heading}-ex2.png'
    return file_name


def image_download(data_set):
    year = data_set['year']
    m_number = data_set['month_number']
    m_name = data_set['month_name']
    resolution = data_set['resolution']
    url = f'https://www.smashingmagazine.com/{year}/{m_number}/desktop-wallpaper-calendars-{m_name}-{year}/'
    try:
        soup = BeautifulSoup(urllib.request.urlopen(url), 'html.parser')
        tags_a = soup.find_all('a', string=data_set['resolution'])
        if len(tags_a) > 0:
            for tag in tags_a:
                try:
                    image_url = tag['href']
                    heading = tag.find_previous(['h4', 'h3']).text
                    file_name = file_name_generate(heading)
                    urllib.request.urlretrieve(image_url, file_name)
                    print(f'Image {file_name} has been successfully downloaded')
                except Exception:
                    print(f'Failure! Image {file_name} was not downloaded')
            return 'Done!'
        else:
            return 'Could not find images for the specified time or resolution'
    except urllib.error.URLError as error:
        if error.reason == 'Not Found':
            return 'URL with specified parameters was not found'
        elif error.reason == '[Errno -2] Name or service not known':
            return 'Сould not follow the link'
        else:
            return error.reason


if __name__ == '__main__':
    # Optionally, I could call inputs in the while true block
    # and check the data with regular expressions
    date_entry = input('Enter a date in YYYY-MM format: ')
    resolution = input('Enter image resolution: ')
    try:
        data_set = get_user_data(date_entry, resolution)
    except Exception:
        exit('Incorrect input')
    print(image_download(data_set))

# tests:


def test_get_user_data():
    with pytest.raises(Exception):
        assert get_user_data('2019 10', '1280:800')


def test_image_download():
    inputs = ('2019-10', '1280x800')
    with mock.patch.object(builtins, 'input', lambda message: next(inputs)):
        date_entry = inputs[0]
        resolution = inputs[1]
        data_set = get_user_data(date_entry, resolution)
        assert image_download(data_set) == 'Done!'


def files_count():
    images_list = os.listdir('/task_2_images')
    assert len(images_list) == 30
