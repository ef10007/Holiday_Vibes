from flask import render_template, request, Response, session, jsonify, make_response, redirect, flash, url_for
from datetime import datetime, date, timedelta
import datetime
from sqlalchemy.orm import subqueryload, joinedload
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import func
from holvflask import app
from holvflask.pro_init_db import db_session, init_database
from holvflask.pro_models import User, City, Country, CityMPT, Preference, Ticket, Weather
from pprint import pprint




@app.route('/calendar/iso')
def calendar_iso():

    # today = date.today()

    # day = datetime.datetime.isocalendar(today)

    day = '2019-4-17'

    return jsonify( {"result": day} )


def daterange(sdate, edate):
    for n in range(int ((edate - sdate).days ) + 1):
        yield sdate + timedelta(n)


@app.route("/mymenu/<userid>", methods=['GET'])
def mymenu_user(userid):

    p = db_session.query(Preference).filter("userid = :userid").params(userid=userid).first()

    return jsonify( p.json() )


@app.route("/mymenu/edit/<userid>", methods=['GET'])
def mymenu_user_edit(userid):

    p = db_session.query(Preference).filter("userid = :userid").params(userid=userid).first()

    if len(p) > 1:
        print("WOOWOWOOWOW")


    return jsonify( p.json() )


@app.route('/mymenu/<start_date>&<end_date>&<cityname>', methods=['GET'])
def mymenu_user_calendar(start_date, end_date, cityname):

    start_date_datetime = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date_datetime = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()

    data = {}
    data['result'] = []

    for d in daterange(start_date_datetime, end_date_datetime):
        datalist = []
        data1 = {}

        days = d.strftime("%Y-%m-%d")

        dwt = db_session.query(Weather).filter("dt = :dt and cityname=:cityname").params(dt=days, cityname=cityname).first()

        dtk = db_session.query(Ticket).filter("dt = :dt and cityname=:cityname").params(dt=days, cityname=cityname).first()


        description = dwt.description
        dmintemp = dwt.mintemp
        dmaxtemp = dwt.maxtemp
        price = dtk.price

        datalist = (description, dmintemp, dmaxtemp, price)

        data1['days'] = days
        data1['desc'] = datalist

        data['result'].append(data1)

        pprint(data)

    return jsonify( data )



@app.route("/mymenu", methods=['GET'])
def mymenu():

    today = date.today()
    dt = today.strftime("%Y-%m-%d")
        
    year = request.args.get('year', date.today().year, int)
    month = request.args.get('month', date.today().month, int)
    namedmonth = today.strftime("%B")
    selected_year = request.args.get('selected_year')
    selected_month = request.args.get('selected_month')
    
    userid = session['loginUser']['id']

    p = db_session.query(Preference).filter("userid = :userid").params(userid=userid).first()

    if p is not None:
        
        username = p.useridfk.username

        return render_template('mymenu.htm', year=year, month=month, dt=dt, namedmonth=namedmonth, selected_year=selected_year, selected_month=selected_month, p=p, userid=userid, username=username)

    
    else:
            
        return render_template('mymenu.htm', year=year, month=month, dt=dt, namedmonth=namedmonth, selected_year=selected_year, selected_month=selected_month, userid=userid)




@app.route("/mymenu", methods=['POST'])
def preference():

    error = None
    userid = session['loginUser']['id']
    
    start_date = request.form.get('startdate')
    end_date = request.form.get('enddate')
    cityname = request.form.get('city')
    temperature = request.form.get('temperature')
    minbud = request.form.get('mininum')
    maxbud = request.form.get('maximum')

    if not start_date:
        error = 'Please select your Start Date.'
    elif not end_date:
        error = 'Please select your End Date.'
    elif not cityname:
        error = 'Please set up your Favorite City.'

    if error is not None:
        flash(error)


    p = Preference(userid, start_date, end_date, cityname, temperature, minbud, maxbud)

    try:
        db_session.add(p)
        db_session.commit()

    except:
        db_session.rollback()
    
    return redirect('/mymenu')

@app.route("/mymenu/edit", methods=['GET'])
def preference_edit_get():

    today = date.today()
    dt = today.strftime("%Y-%m-%d")
        
    year = request.args.get('year', date.today().year, int)
    month = request.args.get('month', date.today().month, int)

    namedmonth = today.strftime("%B")

    selected_year = request.args.get('selected_year')
    selected_month = request.args.get('selected_month')
    
    userid = session['loginUser']['id']
    
    return render_template('mymenu_edit.htm',  year=year, month=month, dt=dt, namedmonth=namedmonth, selected_year=selected_year, selected_month=selected_month, userid=userid)


@app.route("/mymenu/edit", methods=['POST'])
def preference_edit():
    
    userid = session['loginUser']['id']
    
    start_date = request.form.get('startdate')
    end_date = request.form.get('enddate')

    cityname = request.form.get('city')
    temperature = request.form.get('temperature')
    minbud = request.form.get('mininum')
    maxbud = request.form.get('maximum')

    p = Preference(userid, start_date, end_date, cityname, temperature, minbud, maxbud)

    try:
        db_session.merge(p)
        db_session.commit()

    except:
        db_session.rollback()
    
    return redirect('/mymenu')
    


@app.route("/")
def holiday():
    return render_template('main.htm')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.htm')

@app.route("/registration", methods=['GET'])
def registration_get():
    return render_template('regist.htm')

@app.route("/registration", methods=['POST'])
def registration_post():

    email = request.form.get('email')
    passwd = request.form.get('passwd')
    passwd2 = request.form.get('passwd2')
    username = request.form.get('username')

    if db_session.query(User).filter("email = :email").params(email=email).first() is not None:
    
        flash('ERROR: The email is already registered.')
        return render_template('regist.htm', email=email, username=username)

    elif passwd != passwd2:
        flash('ERROR: Your password and confirmation password do not match.')
        return render_template('regist.htm', email=email, username=username)

    else:

        u = User(email, passwd, username)
    
        try:
            db_session.add(u)
            db_session.commit()

        except:
            db_session.rollback()
        
        flash('Welcome, %s! You have successfully signed up.' % username)
        return redirect('/login')


@app.route('/login', methods=['GET'])
def login_get():
    return render_template('login.htm')

@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    passwd = request.form.get('passwd')

    u = db_session.query(User).filter("email = :email and passwd = sha2(:passwd, 256)").params(email=email, passwd=passwd).first()

    if u is not None:
        session['loginUser'] = { 'id': u.id, 'name': u.username }

        if session.get('next'):
            next = session.get('next')
            del session['next']
            return redirect(next)

        return redirect('/')
    else:
        flash('ERROR: Your email or password is not correct.')
        return render_template('login.htm', email=email)

    
@app.route('/logout')
def logout():
    if session.get('loginUser'):
        del session['loginUser']
    
    return redirect('/')


@app.route('/calendar')
def calendar():


    today = date.today()

    day = datetime.datetime.isocalendar(today)
  
    dt = today.strftime("%Y-%m-%d")
    
    year = request.args.get('year', date.today().year, int)
    month = request.args.get('month', date.today().month, int)

    return render_template('calendar.htm', year=year, month=month, day=day)

