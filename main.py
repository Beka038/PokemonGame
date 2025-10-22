import telebot
from random import randint 
from config import token

from logic import Pokemon, Fighter, Wizard

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    #if message.from_user.username not in Pokemon.pokemons.keys():
        chance = randint(0,11)
        if chance == 1:
            pokemon = Fighter(message.from_user.username)
            bot.send_message(message.chat.id, f"Ваш покемон FIGHTER 💪")
        elif chance == 2:
            pokemon = Wizard(message.from_user.username)
            bot.send_message(message.chat.id, f"Ваш покемон WIZARD 💥")
        else:
            pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    #else:
        #bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['attack'])
def fight(message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.username in Pokemon.pokemons.keys() and message.from_user.username in Pokemon.pokemons.keys():
            enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
            pok = Pokemon.pokemons[message.from_user.username]
            res = pok.attack(enemy)
            bot.send_message(message.chat.id, res)
        else:
            bot.send_message(message.chat.id, "Сражатся можно только с покемонами")
    else:
        bot.send_message(message.chat.id, "Чтобы сражатся ответте на сообщение другого пользователя")
    

bot.infinity_polling(none_stop=True)

