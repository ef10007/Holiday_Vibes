from flask import Flask, g, request, Response, make_response, session, render_template, url_for, redirect, flash, jsonify
from datetime import timedelta, date, datetime
import os
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
from holvflask.pro_init_db import init_database, db_session


app = Flask(__name__)

import holvflask.pro_views
import holvflask.pro_filters

app.debug = True
app.config['SERVER_NAME'] = 'localhost.localdomain:5000'

app.config.update(
	SECRET_KEY='X1243yRH!mMwf',
	SESSION_COOKIE_NAME='pyweb_flask_session',
	PERMANENT_SESSION_LIFETIME=timedelta(31)      # 31 days
)

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

