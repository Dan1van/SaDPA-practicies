import datetime
from forex_python.converter import CurrencyRates, RatesNotAvailableError

c = CurrencyRates()


def right_currency(entered_currency: str):
    try:
        c.get_rates(entered_currency)
        return entered_currency != 'RUB'
    except RatesNotAvailableError:
        return False


def right_date_range(entered_date_range: str):
    try:
        if entered_date_range[11] == '-':
            date1, date2 = entered_date_range.split(' - ')
            datetime.datetime.strptime(date1, '%Y-%m-%d')
            datetime.datetime.strptime(date2, '%Y-%m-%d')

            year1, month1, day1 = map(int, date1.split('-'))
            year2, month2, day2 = map(int, date2.split('-'))
            date1 = datetime.date(year1, month1, day1)
            date2 = datetime.date(year2, month2, day2)
            return date1 < date2
    except (IndexError, ValueError):
        return False

