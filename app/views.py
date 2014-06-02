#========================================
#views.py
#lead (and only) developer: Bobby Joe 3.0
#views script for three_views Flask app
#========================================

# -*- coding: utf-8 -*-

from app import app
from flask import render_template

@app.route('/')
@app.route('/home')
@app.route('/index')
@app.route('/view_1')
def view_1():
	return render_template('three_views_index.html')

@app.route('/view_2')
def view_2():
	return render_template('three_views_2.html')

@app.route('/views_3')
def view_3():
	return render_template('three_views_3.html')