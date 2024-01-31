't.me/CrBotTest_bot. тестовый бот'

import json
import requests
import telebot

TOKEN = '6976649854:AAHOVlUejL8_qrboZSWxwN-JZZO9-2gc9j8'

bot = telebot.TeleBot(TOKEN)

# @bot.message_handler()
# def echo_test(message: telebot.types.Message):
#     bot.send_message(message.chat.id, 'hello')

keys = {
    'биткоин': 'BTC',
    'эфириум': 'ETH',
    'д': 'USD'
}  #

class ConvertionException(Exception):
    pass


# class CryptoConverter:
#     @staticmethod
#     def converter(self):




@bot.message_handler(commands=['start', 'help'])  # Описываем help
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем ' \
           'формате:\n<имя валюты> ' \
           '<в какую валуту перевести> ' \
           '<количество переводимой валюты>' \
           '\nУвидеть список всех доступных валют: /values'

    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])  # Описываем Запрос "Значения"
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))  # (text, key, ) - кортеж. Почему не список?
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])  # Описываем Запрос "Конвертация"
def convert(message: telebot.types.Message):  #  Получаем сообщение
    # quote, base, amount = message.text.split(' ')  #  Получаем переменные из сообщения
    values = message.text.split(' ')  #  Получаем переменные из сообщения

    if len(values) > 3:
        raise ConvertionException('Слишком много параметров')
        # raise Exception('Слишком много параметров')

    quote, base, amount = values

    if quote == base:
        raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

    try:
        quote_ticker = keys[quote]
    except KeyError:
        raise ConvertionException(f'Не удалось обработать валюту {quote}')
    try:
        base_ticker = keys[base]
    except KeyError:
        raise ConvertionException(f'Не удалось обработать валюту {base}')
    try:
        amount = float(amount)
    except ValueError:
        raise ConvertionException(f'Не удалось обработать количество {amount}')



    r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')  # Отправляем запрос API, присваиваем ответ переменной r
    # text = json.loads(r.content)[keys[base]]  #  преобразуем ответ в текст
    total_base = json.loads(r.content)[keys[base]]  #  преобразуем ответ в текст
    text = f'Цена {amount} {quote} в {base} - {total_base}'
    bot.send_message(message.chat.id, text)  #  отправляем текст ответа пользователю




bot.polling()  # Запускаем бота

# Тестовый запрос через Python Console
# r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD')
# r.content
# exit()
