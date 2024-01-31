'''t.me/CrBotTest_bot. тестовый бот.
Добавлен класс Proper.
Если пользователь ввёл несуществующую валюту, Proper помагает найти подходящую'''

import telebot
from config import keys, TOKEN
from extensions import ConvertionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)


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
def convert(message: telebot.types.Message):  # Получаем сообщение
    try:
        values = message.text.split(' ')  # Получаем переменные из сообщения
        if len(values) != 3:
            raise ConvertionException('Неверное количество параметров')
        quote, base, amount = values
        total_base = CryptoConverter.converter(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя. \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)  # отправляем текст ответа пользователю


bot.polling()  # Запускаем бота

# Тестовый запрос через Python Console
# r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD')
# r.content
# exit()
