from flask import Flask, render_template, request, redirect, jsonify, \
    url_for, flash

from flask_bootstrap import Bootstrap

# from sqlalchemy import create_engine, asc, desc, \
#     func, distinct
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.serializer import loads, dumps

# from database_setup import Base, Things

import random
import string
import logging
import json
import httplib2
import requests


app = Flask(__name__)
bootstrap = Bootstrap(app)


# Connect to database and create database session
# engine = create_engine('sqlite:///flaskstarter.db')
# Base.metadata.bind = engine

# DBSession = sessionmaker(bind=engine)
# session = DBSession()


# Display all things
@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/home')
def indexPage():
    return render_template('index.html')

@app.route('/about')
def aboutPage():
    return render_template('about.html')

@app.route('/service')
def servicePage():
    return render_template('page-service-list.html')

@app.route('/contact')
def contactPage():
    return render_template('contact.html')

@app.route('/request')
def requestPage():
    return render_template('request.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run()
