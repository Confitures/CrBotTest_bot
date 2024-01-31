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
    def converter(base: str, quote: str, amount: str) -> float:

        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote = quote.lower()
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}. \n'
                                      f'Возможно, Вы ищете: {Proper.find(quote)}')
        try:
            base = base.lower()
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}. \n'
                                      f'Возможно, Вы ищете: {Proper.find(base)}')
        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        r = requests.get(
            f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')  # Отправляем запрос API, присваиваем ответ переменной r
        total_quote = json.loads(r.content)[keys[quote]]  # вынимаем из ответа значение в float
        total_quote *= amount
        return total_quote


if __name__ == "__main__":
    print('___________test 01')
    base, quote, amount = 'биткоин', 'доллар', '1'
    total_base = CryptoConverter.converter(base, quote, amount)
    print(f'type(total_base) = {type(total_base)}')
    print(total_base)

    print('___________test 02')
    base, quote, amount = 'биткоин', 'доллар', '0.0001'
    total_base = CryptoConverter.converter(base, quote, amount)
    print(total_base)

    print('___________test 03')
    base, quote, amount = 'БИТКОИн', 'доллар', '0.0001'
    total_base = CryptoConverter.converter(base, quote, amount)
    print(total_base)

    print('___________test 04')
    base, quote, amount = 'бит', 'доллар', '0.0001'
    total_base = CryptoConverter.converter(base, quote, amount)
    print(total_base)

    # print('___________test 05')
    # base, quote, amount = 1, 'доллар', '0.0001'
    # total_base = CryptoConverter.converter(base, quote, amount)
    # print(total_base)
