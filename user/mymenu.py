from datetime import datetime, date

today = date.today() # datetime.date 
  
dt = today.strftime("%Y-%m-%d") # str

def temp(start, end):
    lst = []

    for i in range(start, end+1):
        lst.append(i)
    print(lst)

temp(10,24) # spring
temp(25,40) # summer
temp(5,25) # autumn
temp(-15,4) # winter


def make_date(dt, fmt):
    if not isinstance(dt, date):
        return datetime.strptime(dt, fmt)
    else:
        return dt

def namedmonth(dt, fmt='%Y-%m-%d'):


    namedmonths = dt.strptime("%B")

    print(namedmonths)

    # return d.month
today = date.today()
  
dt = today.strftime("%Y-%m-%d")
namedmonth(dt)