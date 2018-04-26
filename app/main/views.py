from flask import render_template,request,redirect,url_for, jsonify
from . import main
import paypalrestsdk

# Views
@main.route('/')
def index():
	title = 'Flask Base'
	return render_template('index.html',title = title)

@main.route('/payment', methods=['POST'])
def payment():
	payment = paypalrestsdk.Payment({
		"intent": "sale",
		"payer": {
			"payment_method": "paypal"},
		"redirect_urls": {
			"return_url": "http://localhost:3000/payment/execute",
			"cancel_url": "http://localhost:3000/"},
		"transactions": [{
			"item_list": {
				"items": [{
					"name": "testitem",
					"sku": "12345",
					"price": "500.00",
					"currency": "USD",
					"quantity": 1}]},
			"amount": {
				"total": "500.00",
				"currency": "USD"},
			"description": "This is the payment transaction description."}]})
	
	if payment.create():
		print('Payment success!')
	else:
		print(payment.error)
	

	
	return jsonify({'paymentID': payment.id})