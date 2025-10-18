from random import randint, choice
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.name = self.get_name()
        self.shiny = self.shiny_pokemon()
        self.img = self.get_img()
        
        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon-form/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites'][f'front_{self.shiny}'])
    
    def shiny_pokemon(self):
        random_v2 = choice([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
        if random_v2 == 1:
            self.shiny = 'shiny'
            self.name = self.name + '  |  💫 Легендарный !'
            return self.shiny
        else:
            self.shiny = 'default'
            return self.shiny
    
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pika Pika Pika Chu Shuchu Ne rabotaet"


    # Метод класса для получения информации
    def info(self):
        return f'''
            Имя твоего покеомона: {self.name}
            '''

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img



