
from pip._vendor import requests

def get_pokemon(pokemon):
    return requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}").json()


class pokemon_info:
    universe = 'pokemon universe'

    def __init__(self, type, name, height, weight, attack, speed):
        self.type = type
        self.name = name
        self.height = height
        self.weight = weight
        self.attack = attack
        self.speed = speed

    def abilities(self):
        print(f'{self.name}) posseses a special attach called {self.attack}')

    @classmethod
    def location(cls):
        print(F'all pokemon live in the beautiful {cls.universe}')



get =  get_pokemon('haunter')

haunter_name = get['name']
haunter_type = get['types'][0]['type']['name']
haunter_height = get['height']
haunter_weight = get['weight']
haunter_weight = get['weight']
haunter_attack = get['abilities'][0]['ability']['name']
haunter_speed = get['stats'][0]['stat']['name']

haunter = pokemon_info(haunter_type, haunter_name, haunter_height, haunter_weight, haunter_attack, haunter_speed)



get2 =  get_pokemon('pikachu')

pikachu_name = get2['name']
pikachu_type = get2['types'][0]['type']['name']
pikachu_height = get2['height']
pikachu_weight = get2['weight']
pikachu_weight = get2['weight']
pikachu_attack = get2['abilities'][0]['ability']['name']
pikachu_speed = get2['stats'][0]['stat']['name']

pikachu = pokemon_info(pikachu_type, pikachu_name, pikachu_height, pikachu_weight, pikachu_attack, pikachu_speed)


get3 =  get_pokemon('charizard')

charizard_name = get3['name']
charizard_type = get3['types'][0]['type']['name']
charizard_height = get3['height']
charizard_weight = get3['weight']
charizard_weight = get3['weight']
charizard_attack = get3['abilities'][0]['ability']['name']
charizard_speed = get3['stats'][0]['stat']['name']

pikachu = pokemon_info(charizard_type, charizard_name, charizard_height, charizard_weight, charizard_attack, charizard_speed)


get4 = get_pokemon('mew')

mew_name = get4['name']
mew_type = get4['types'][0]['type']['name']
mew_height = get4['height']
mew_weight = get4['weight']
mew_weight = get4['weight']
mew_attack = get4['abilities'][0]['ability']['name']
mew_speed = get4['stats'][0]['stat']['name']

pikachu = pokemon_info(mew_type, mew_name, mew_height, mew_weight, mew_attack, mew_speed)


get5 =  get_pokemon('pidgeotto')

pidgeotto_name = get5['name']
pidgeotto_type = get5['types'][0]['type']['name']
pidgeotto_height = get5['height']
pidgeotto_weight = get5['weight']
pidgeotto_weight = get5['weight']
pidgeotto_attack = get5['abilities'][0]['ability']['name']
pidgeotto_speed = get5['stats'][0]['stat']['name']

pikachu = pokemon_info(pidgeotto_type, pidgeotto_name, pidgeotto_height, pidgeotto_weight, pidgeotto_attack, pidgeotto_speed)