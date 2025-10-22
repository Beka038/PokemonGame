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
        
        self.hp = randint(75, 101)
        self.power = randint(15,30)
        
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
        
        
    def attack(self, enemy):
        if enemy.hp > self.power:
            enemy.hp -= self.power
            self.hp -= enemy.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "

    # Метод класса для получения информации
    def info(self):
        return f'''
            Имя твоего покеомона: {self.name}
            Здоровья: {self.hp}
            Урон: {self.power}
            
            '''#free place for class of the pokemon Fighter or Wizard


class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(5,15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f"\nБоец применил супер-атаку силой:{super_power}"
    def info(self):
        info_and_pokemon_type = super().info(self) + 'Вид покемона: Wizard  '
        return f'''
            Твой покемон: {info_and_pokemon_type}
    '''

class Wizard(Pokemon):
    def attack(self, enemy):
        chance = randint(0,4)
        if chance==1:
            shield = randint(10, 20)
            self.hp += shield
            return super().attack(enemy) + f"\nБоец использовал щит на: {shield}"
        else:
            return super().attack(enemy)
            
    def info(self):
        info_and_pokemon_type = super().info(self) + 'Вид покемона: Wizard  '
        return f'''
            Твой покемон: {info_and_pokemon_type}
    '''

