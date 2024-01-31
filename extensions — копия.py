import json
import requests
from config import keys
from difflib import SequenceMatcher


class ConvertionException(Exception):
    pass


class Proper():
    @staticmethod
    def find(req: str) -> str:
        'Возвращает ключ из словаря keys, сходный с req'
        df = 0
        proper = str()
        for k in keys.keys():
            var = SequenceMatcher(None, k, req).quick_ratio()
            if var > df:
                df = var
                proper = k
        return proper


class CryptoConverter:
    @staticmethod
    def converter(quote: str, base: str, amount: str) -> float:

        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote = quote.lower()
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}. \n'
                                      f'Возможно, Вы ищете: {Proper.find(quote)}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}. \n'
                                      f'Возможно, Вы ищете: {Proper.find(base)}')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        r = requests.get(
            f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')  # Отправляем запрос API, присваиваем ответ переменной r
        total_base = json.loads(r.content)[keys[base]]  # вынимаем из ответа значение в float
        print(f'type(total_base) = {type(total_base)}')
        total_base *= amount
        return total_base


if __name__ == "__main__":
    print('___________test 01')
    quote, base, amount = 'биткоин', 'доллар', '1'
    total_base = CryptoConverter.converter(quote, base, amount)
    print(f'type(total_base) = {type(total_base)}')
    print(total_base)

    print('___________test 02')
    quote, base, amount = 'биткоин', 'доллар', '0.0001'
    total_base = CryptoConverter.converter(quote, base, amount)
    print(total_base)

    print('___________test 03')
    quote, base, amount = 'БИТКОИн', 'доллар', '0.0001'
    total_base = CryptoConverter.converter(quote, base, amount)
    print(total_base)

    # print('___________test 04')
    # quote, base, amount = 'бит', 'доллар', '0.0001'
    # total_base = CryptoConverter.converter(quote, base, amount)
    # print(total_base)

    # print('___________test 05')
    # quote, base, amount = 1, 'доллар', '0.0001'
    # total_base = CryptoConverter.converter(quote, base, amount)
    # print(total_base)
