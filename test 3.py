import telebot
from config import keys, TOKEN
from extensions import ConvertionException, CryptoConverter


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text', ])  # Описываем Запрос "Конвертация"
def convert(message: telebot.types.Message):  # Получаем сообщение
        print(message)
        print(type(message))
        print(f'messge.text = {message.text}')
        values = message.text.split(' ')  # Получаем переменные из сообщения
        print(f'values = {values}')
        print(f'type of values = {type(values)}')

        quote, base, amount = values
        print()
        print(quote, base, amount)

        bot.reply_to(message, f'Ошибка пользователя. \n{values}')
    # except Exception as e:
    #     bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    # else:
    #     text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, quote)  # отправляем текст ответа пользователю


bot.polling()  # Запускаем бота

# test1 test2 3