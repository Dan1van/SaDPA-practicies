import pandas as pd
import matplotlib.pyplot as plt
from forex_python.converter import CurrencyRates

from prac1.verify_data import right_currency
from prac1.verify_data import right_date_range

c = CurrencyRates()
plt.close('all')


def enter_currency():
    while True:
        entered_currency = input('Введите валюту:\n')

        if right_currency(entered_currency):
            return entered_currency
        else:
            print('Введена неверная валюта! Попробуйте снова\n')
            continue


def enter_date_range():
    while True:
        entered_date_range = input('Введите период дат, за который требуется построить график:\n'
                                   '(Период вводить в формате: "ГГГГ-ММ-ДД - ГГГГ-ММ-ДД". Где первая дата - начало, вторая - конец)\n')

        if right_date_range(entered_date_range):
            return entered_date_range.split(' - ')
        else:
            print('Введен неверный период! Попробуйте снова\n')
            continue


def enter_step():
    step_dict = {'1': 'D', '2': 'W', '3': 'M', '4': 'Y'}
    while True:
        entered_num = input('Введите номер шага:\n'
                            '\n'
                            '1. День\n'
                            '2. Неделя\n'
                            '3. Месяц\n'
                            '4. Год\n')

        if entered_num in step_dict:
            return step_dict[entered_num]
        else:
            print('Введен неверный номер шага! Попробуйте снова\n')
            continue


def main():
    currency = enter_currency()
    date_start, date_end = enter_date_range()
    step = enter_step()

    date_range = pd.date_range(start=date_start, end=date_end, freq=step)

    currency_ratio = []
    for date in date_range:
        currency_ratio.append(c.get_rate(currency, 'RUB', date))

    fig, ax = plt.subplots(figsize=(16, 9))

    df = pd.DataFrame(data=currency_ratio, index=date_range)

    short_rolling = df.rolling(window=20).mean()
    long_rolling = df.rolling(window=100).mean()

    ax.plot(date_range, currency_ratio, label=f'Курс')
    ax.plot(short_rolling, label='20')
    ax.plot(long_rolling, label='100')
    ax.legend(loc='best')
    ax.set_ylabel(f'Курс {currency} к RUB')

    fig.show()


if __name__ == '__main__':
    main()
