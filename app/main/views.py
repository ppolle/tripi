from flask import render_template,request,redirect,url_for, jsonify
from . import main

# Views
@main.route('/')
def index():
	title = 'Flask Base'
	return render_template('index.html',title = title)

@main.route('/payment', methods=['POST'])
def payment():

	return jsonify({'paymentID': 'PAYMENTID'})