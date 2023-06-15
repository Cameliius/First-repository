import requests

url = 'https://swapi.dev/api'

response = requests.get(url).json()

starships_api = response.get('starships')


def check_starships(url):
    count_find = 0
    idd = 1
    starships = []
    while count_find != 5:
        response = requests.get(url + '/' + str(idd)).json()
        idd += 1
        if response.get('detail') != 'Not found':
            count_find += 1
            speed = response.get('max_atmosphering_speed')
            name = response.get('name')
            if speed.isalnum():
                starships.append([int(speed), name])
    max_speed = starships[0][0]
    name_max_speed = starships[0][1]
    for i in range(1, len(starships)):
        if starships[i][0] > max_speed:
            max_speed = starships[i][0]
            name_max_speed = starships[i][1]
    print(max_speed, name_max_speed)


check_starships(starships_api)
