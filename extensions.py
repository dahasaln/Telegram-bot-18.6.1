import json
import requests
from config import *
class ExchangeException(Exception):
    pass


class Exchange:
    @staticmethod
    def get_price(currency: str, money: str, num: str):
        if currency == money:
            raise ExchangeException(
                f'Нельзя перевести одинаковые валюты {money}.')

        try:
            currency_ticker = keys[currency]
        except KeyError:
            raise ExchangeException(f'Не смог обработать валюту {currency} . Введите команду /values или 3 параметра.'
                                    f'\n Например: рубль евро 1 ')

        try:
            money_ticker = keys[money]
        except KeyError:
            raise ExchangeException(f'Не смог обработать валюту {money} . Введите команду /values или 3 параметра.'
                                    f'\n Например: рубль евро 1 ')


        try:
            if int (num) > 0:
                num = int(num)
            else:
                raise ExchangeException (f'Количество не может быть отрицательным: {num}. '
                                    f'\nВведите 3 параметра.'
                                    f'\n Например: рубль евро 1 ')
        except ValueError:
            raise ExchangeException(f'Не смог обработать валюту {num} . Введите команду /values или 3 параметра.'
                                    f'\n Например: рубль евро 1 ')


        r = requests.get(
            f'https://min-api.cryptocompare.com/data/price?fsym={money_ticker}&tsyms={currency_ticker}')
        total_money = float(json.loads(r.content)[keys[currency]])
        return total_money
