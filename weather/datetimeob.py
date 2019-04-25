from datetime import datetime, date, timedelta

today = date.today()

dt = today.strftime("%Y-%m-%d")

year = date.today().year
month = date.today().month
day = date.today().day


def daterange(date1, date2):
    for n in range(int ((date2 - date1).days) + 1):
        yield date1 + timedelta(n)

start_dt = date(2015, 12, 20)

# print(type(date(2015, 12, 20))) #<class 'datetime.date'>
end_dt = date(2016, 1, 11)


# for dt in daterange(start_dt, end_dt):
#     print("HERE", dt.strftime("%Y-%m-%d"))
	



import pandas as pd
from pprint import pprint

datelist = pd.date_range(pd.datetime.today(), periods=365).tolist()
# pprint(type(datelist)) #list

# for lst in datelist:
    # pprint(type(lst))

    
# year = request.args.get('year', date.today().year, int)
# month = request.args.get('month', date.today().month, int)
