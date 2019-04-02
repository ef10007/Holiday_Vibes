from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
from holvflask import app


def make_date(dt, fmt):
    if not isinstance(dt, date):
        return datetime.strptime(dt, fmt)
    else:
        return dt

@app.template_filter('ymd')               # cf. Handlebars' helper
def datetime_ymd(dt, fmt='%m-%d'):
    if isinstance(dt, date):
        return "<strong>%s</strong>" % dt.strftime(fmt)
    else:
        return dt


@app.template_filter('simpledate')
def simpledate(dt):
    if not isinstance(dt, date):
        dt = datetime.strptime(dt, '%Y-%m-%d %H:%M')

    if (datetime.now() - dt).days < 1:
        fmt = "%H:%M"
    else:
        fmt = "%m/%d"

    return "<strong>%s</strong>" % dt.strftime(fmt)


@app.template_filter('sdt')
def sdt(dt, fmt='%Y-%m-%d'):
    d = make_date(dt, fmt)
    wd = d.weekday()
    return (1 if wd == 6 else wd) * -1


@app.template_filter('month')
def month(dt, fmt='%Y-%m-%d'):
    d = make_date(dt, fmt)
    return d.month


@app.template_filter('year')
def year(dt, fmt='%Y-%m-%d'):
    d = make_date(dt, fmt)
    return d.year

@app.template_filter('namedmonth')
def namedmth():
    today = date.today()
    namedmonth = today.strftime("%B")

    return namedmonth

@app.template_filter('edt')
def edt(dt, fmt='%Y-%m-%d'):
    d = make_date(dt, fmt)
    nextMonth = d + relativedelta(months=1)
    return (nextMonth - timedelta(1)).day + 1
