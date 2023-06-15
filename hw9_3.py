import requests
from bs4 import BeautifulSoup

# Получаем список жанров
count = 0
genres_names_disct = {}
response = requests.get('https://store.steampowered.com/?l=russian')
response = response.content

html = BeautifulSoup(response, 'html.parser')
genres = html.find_all('div', class_='popup_genre_expand_content responsive_hidden')
for genre in genres:
    for content in genre.contents:
        if content != '\n':
            if count > 40:
                break
            url = content.attrs['href']
            genre_name = content.contents[0]
            genres_names_disct[count] = [genre_name, url]
            # print(url, genre_name)
            count += 1

# Выводим список жанров на экран
print('Список доступных жанров')
for key in genres_names_disct:
    print(f'{key} {genres_names_disct[key][0]}')

genre_input = int(input('Пожалуйста, введи номер интересующего тебя жанра:'))
genre_input_name = genres_names_disct[genre_input][0]
genre_input_url = genres_names_disct[genre_input][1]

print(f'''\nТы можешь посмотреть игры жанра '{genre_input_name}' перейдя по следующей ссылке: {genre_input_url}''')
