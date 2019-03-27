from flask import render_template, request, Response, session, jsonify, make_response, redirect, flash, url_for
from datetime import datetime, date
from sqlalchemy.orm import subqueryload, joinedload
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import func
from holvflask import app
from holvflask.pro_init_db import db_session, init_database
from holvflask.pro_models import User, City, Country, CityMPT



@app.route('/calendar')
def calendar():
    today = date.today()
  
    dt = date.today().strftime("%Y-%m-%d")
    
    year = request.args.get('year', date.today().year, int)
    month = request.args.get('month', date.today().month, int)

    return render_template('calendar.htm', year=year, month=month)


@app.route("/")
def holiday():
    return render_template('main.htm')

@app.route("/mymenu", methods=['GET'])
def mymenu():

    countries = Country.query.order_by(Country.countryname).all()
    cities = CityMPT.query.all()

    if request.is_xhr:
        return jsonify([c.json() for c in cities])

    return render_template('mymenu.htm', countries=countries, cities=cities)

@app.route('/getcities?=<country_name>', methods=['GET'])
def getcities(country_name):

    cities = CityMPT.query.filter_by(mpt_contryname=country_name).all()

    print(cities)

    if request.is_xhr:
        return jsonify([c.json() for c in cities])

    return render_template('mymenu.htm', cities=cities)


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
        # print(u)
        try:
            db_session.add(u)
            db_session.commit()

            # print(u)
        
        except:
            db_session.rollback()
        
        flash('Welcome, %s!' % username)
        return redirect('/login')


@app.route('/login', methods=['GET'])
def login_get():
    return render_template('login.htm')

@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    passwd = request.form.get('passwd')

    u = User.query.filter('email = :email and passwd = :passwd').params(email=email, passwd=passwd).first()
    
    print("HIIIIIIIIIIIIIIIIIIIIIIII")

    if u is not None:
        session['loginUser'] = { 'useremail': u.email, 'name': u.username }

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