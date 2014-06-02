#=============================================
#__init__.py
#lead (and only) developer: Bobby Joe 3.0
#initializing script for three_views Flask app
#=============================================

# -*- coding: utf-8 -*-

from flask import Flask 

app = Flask(__name__)
app.config.from_object('config')

from app import views