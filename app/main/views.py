from flask import render_template,request,redirect,url_for
from . import main
from app.request import distance_matrix

# Views
@main.route('/')
def index():
	title = 'Flask Base'
	destinations = distance_matrix(chrome, 'lagos', 'Nigeria')
	origins = distance_matrix
	return render_template('index.html',title = title, destinations=destinations, origins=origins)
