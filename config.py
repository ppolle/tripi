import os

class Config:
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	UPLOADED_PHOTOS_DEST ='app/static/photos'
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alexander:lazypass@localhost/tripi'

	DISTANCE_BASE_URL = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins={}&destinations={}&mode=driving&language=en-EN&key=AIzaSyBqbV13-4TJrFXeeBFXiRxilkKBYUb7lMQ'
	DISTANCE_API_KEY = os.environ.get('DIRECTIONS_API_KEY')
	SECRET_KEY = os.environ.get("SECRET_KEY")
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
	MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
	

	@staticmethod
	def init_app(app):
		pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
