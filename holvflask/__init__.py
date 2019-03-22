from flask import Flask, g, request, Response, make_response, session, render_template, url_for, redirect, flash, jsonify
from datetime import timedelta, date, datetime
import os
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta


app = Flask(__name__)

from holvflask.pro_filters import *

from holvflask.pro_init_db import init_database, db_session

from holvflask.pro_models import Country, User, CityMPT

app.debug = True
app.config['SERVER_NAME'] = 'localhost:5000'

app.config.update(
	SECRET_KEY='X1243yRH!mMwf',
	SESSION_COOKIE_NAME='pyweb_flask_session',
	PERMANENT_SESSION_LIFETIME=timedelta(31)      # 31 days
)


@app.route('/calendar')
def calendar():
    today = date.today()
  
    dt = date.today().strftime("%Y-%m-%d")
    
    year = request.args.get('year', date.today().year, int)
    month = request.args.get('month', date.today().month, int)

    return render_template('calendar.htm', year=year, month=month, dt=dt)


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
        u = User(email, passwd, username, True)
        try:
            db_session.add(u)
            db_session.commit(u)
        
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
    u = User.query.filter('email = :email and passwd = sha2(:passwd, 256)').params(email=email, passwd=passwd).first()
    
    if u is not None:
        session['loginUser'] = { 'userid': u.id, 'name': u.username }

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

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


# select 'sss', sha2('sss',256); =password format in mysql

