import datetime

def get_last_weekdays():
    """
    返回上周的日期
    """
    today = datetime.date.today()
    start_date = today - datetime.timedelta(days=today.weekday()+7)
    for i in range(7):
        yield (start_date + datetime.timedelta(days=i)).strftime('%Y%m%d')


if __name__ == '__main__':
    for day in get_last_weekdays():
        print(day)
    # print(get_last_weekdays())