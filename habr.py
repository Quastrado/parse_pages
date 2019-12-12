import urllib.request
from urllib.parse import urlparse

from bs4 import BeautifulSoup

def get_posts(url, limit):
    req = urllib.request.urlopen(url)
    soup = BeautifulSoup(req, 'html.parser')
    posts = soup.find_all('article', {'class': 'post post_preview'}, limit=limit)
    return posts
    

def generate_data(posts):
    for post in posts:
        data = {
            'Заголовок': post.find('h2', {'class': 'post__title'}).text.upper().strip(),
            'Краткое описание': post.find('div', {
                'class': 'post__text post__text-html js-mediator-article'
                }).text.strip(),
            'Дата публикации': post.find('span', {'class': 'post__time'}).text.strip(),
            'Автор': post.find('a', {'title': 'Автор публикации'}).text.strip()
        }
        print('***')
        for k in data.keys():
            if k == 'Краткое описание':
                print(f'{k}:\n{data[k]}\n')
            else:
                print(f'{k}: {data[k]}')
        print('\n')
        

if __name__ == '__main__':
    while True:
        try:
            number_of_posts = int(input('Enter number of posts: '))
            break
        except ValueError:
            print('Incorrect input')
    start_url = 'https://habr.com/ru/top/yearly/'
    try:
        posts = get_posts(start_url, number_of_posts)
        for n in range(2, 50):
            if len(posts) < number_of_posts:
                limit = number_of_posts - len(posts)
                next_url = f'https://habr.com/ru/top/yearly/page{n}/'
                print(next_url)
                next_posts = get_posts(next_url, limit)
                posts = posts + next_posts
            else:
                break
        generate_data(posts)
    except Exception as e:
        exit(e.reason)
    if len(posts) < number_of_posts:
        print("""\nThe specified number exceeds the total number of publications.
            Showing {length} of {number} posts""".format(
                length=len(posts),
                number = number_of_posts)
            )

# https://habr.com/ru/top/yearly/
# заголовок поста
# краткое описание поста
# дата публикации
# имя автора поста