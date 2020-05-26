import telebot
import config
import os
import random

from telebot import types 

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):

	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Картинка")
	
	markup.add(item1)

	bot.send_message(message.chat.id, "Привет👋, {0.first_name}!\nЯ <b>{1.first_name}</b>, который будет отправлять тебе каждый раз новую красивую картинку с новой цитатой. Просто нажми на кнопку Картинка внизу".format(message.from_user, bot.get_me()), 
        parse_mode = 'html', reply_markup = markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
		if message.chat.type == 'private':
			if message.text == 'Картинка':

				otmazki = ['«Если вы всегда спешите, то можете пропустить чудо.» Люис Керролл', 
				'«Поверь в тот факт, что есть ради чего жить, и твоя вера поможет этому факту свершиться.» Уильям Джеймс', 
				'«Чтобы дойти до цели, надо прежде всего идти.» Оноре де Бальзак', 
				'«Каково предназначение человека? Быть им.» Станислав Лец', 
				'«Знание — сокровищница, но ключ к ней — практика.» Фуллер Томас', 
				'«Жизнь — это не страдание. Это просто ты страдаешь ею, вместо того чтобы жить и радоваться ей.» Дэн Миллмен',
				'«Судьба человека, который сидит сиднем, тоже с места не двигается.» Филип Фармер',
				'«Нет смысла в поиске места, где вам будет хорошо. Есть смысл научиться создавать это хорошо в любом месте…»',
				'«Ты не можешь менять направление ветра, но всегда можешь поднять паруса, чтобы достичь своей цели.» Оскар Уайлд',
				'«Когда тебе станет очень худо — подними голову. Ты обязательно увидишь солнечный свет.» Дрю Берримор',
				'«Пока мы крутим педали и рулим к цели, важно не забывать о прекрасном, открывающемся перед нами каждый день.» Пауло Коэльо',
				'«Жизнь прекрасна, когда творишь ее сам.» Софи Марсо']

				random_message = random.choice(otmazki)

				all_files_in_directory = os.listdir('pictures')
				file = random.choice(all_files_in_directory)
				doc = open('pictures/' + '/' + file, 'rb')
				#если нужно подпись к фото
				caption = random_message
				#send_random_photo
				
				bot.send_photo(message.chat.id, doc, caption)
			
			else:
				bot.send_message(message.chat.id, 'Я не знаю что ответить, пусичка 😢')

bot.polling(none_stop=True)

# //banners.adfox.ru/transparent.gif