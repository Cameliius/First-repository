import vk_api
from course import *
import requests


def get_planet():
    planets_all = []
    next_page = 'https://swapi.dev/api/planets/'

    while next_page:
        response = requests.get(next_page).json()
        next_page = response.get('next')
        planets = response.get('results')
        for planet in planets:
            name = planet.get('name')
            diameter = planet.get('diameter')
            if diameter != 'unknown':
                planets_all.append([name, int(diameter)])

    planets_all = sorted(planets_all, key=lambda x: x[1], reverse=True)

    return planets_all[0][0]


def get_starship():
    starships_all = []
    next_page = 'https://swapi.dev/api/starships/'

    while next_page:
        response = requests.get(next_page).json()
        next_page = response.get('next')
        starships = response.get('results')
        for starship in starships:
            name = starship.get('name')
            max_atmosphering_speed = starship.get('max_atmosphering_speed')
            if max_atmosphering_speed.isnumeric():
                starships_all.append([name, int(max_atmosphering_speed)])

    starships_all = sorted(starships_all, key=lambda x: x[1], reverse=True)

    return starships_all[0][0]


token = 'vk1.a.EUXNxhXrRnDAAn2p7rIVdqv8IVdyJxFarxAZpwbaqYfXOBKkUTZOBGge0dRf9ZHmIbKQEmuHtdLQAHuOKUZnXMY2-HuFzs6IQA9sD8eP2CddMtzxKqK6OESd3rRf1ImFhDCyXKn9dFhnhOBV7AhcJezAZUYta8Q_uVC__K7s8Q6C28SemCKZzncQDOjvN_WI8gfsHXfY7Kng-xC0DUZzoA'

vk = vk_api.VkApi(token=token)

while True:
    messages = vk.method('messages.getConversations', {'count': 20, 'filter': 'unanswered'})
    if messages['count'] >= 1:
        print(messages)
        user_id = messages['items'][0]['last_message']['from_id']
        message_id = messages['items'][0]['last_message']['id']
        message_text = messages['items'][0]['last_message']['text']
        if message_text.lower() == 'курс доллара':
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': get_course('R01235')})
        if message_text.lower() == 'планеты':
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': get_planet()})
        if message_text.lower() == 'корабли':
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': get_starship()})
        else:
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': 'Неизвестная команда'})
