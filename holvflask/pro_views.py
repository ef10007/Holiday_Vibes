from flask import render_template, request, Response, session, jsonify, make_response, redirect, flash, url_for
from datetime import datetime, date
from sqlalchemy.orm import subqueryload, joinedload
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import func
from holvflask import app
from holvflask.pro_init_db import db_session, init_database
from holvflask.pro_models import User, City, Country, CityMPT, Preference, Ticket


@app.route('/calendar')
def calendar():

    today = date.today()
  
    dt = today.strftime("%Y-%m-%d")
    
    year = request.args.get('year', date.today().year, int)
    month = request.args.get('month', date.today().month, int)

    return render_template('calendar.htm', year=year, month=month)


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
        start_date = p.start_date
        end_date = p.end_date
        cityname = p.cityname
        temperature = p.temperature
        minbud = p.minbud
        maxbud = p.maxbud

        return render_template('mymenu.htm', year=year, month=month, dt=dt, namedmonth=namedmonth, selected_year=selected_year, selected_month=selected_month, p=p, username=username, start_date=start_date, end_date=end_date, cityname=cityname, temperature=temperature, minbud=minbud, maxbud=maxbud)
    
    else:
        
        return render_template('mymenu.htm', year=year, month=month, dt=dt, namedmonth=namedmonth, selected_year=selected_year, selected_month=selected_month)


@app.route("/mymenu", methods=['POST'])
def preference():
    
    userid = session['loginUser']['id']
    
    start_date = request.form.get('startdate')
    end_date = request.form.get('enddate')

    cityname = request.form.get('city')
    temperature = request.form.get('temperature')
    minbud = request.form.get('mininum')
    maxbud = request.form.get('maximum')


    p = Preference(userid, start_date, end_date, cityname, temperature, minbud, maxbud)

    try:
        db_session.add(p)
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

    if passwd != passwd2:
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