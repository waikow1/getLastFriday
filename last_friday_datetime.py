import datetime
import sys
from dateutil.relativedelta import FR, relativedelta


def get_last_friday(d):
    try:
        d = datetime.datetime.strptime("01/" + d, "%d/%m/%Y")
    except ValueError:
        return 'Ввели не правильное значение'

    res = d + relativedelta(day=31, weekday=FR(-1))
    return res.strftime("%d.%m.%Y")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(get_last_friday(sys.argv[1]))
    else:
        print('Вы не ввели дату')


