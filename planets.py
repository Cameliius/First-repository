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
print(get_starship())