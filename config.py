import os
import paypalrestsdk


class Config:
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	UPLOADED_PHOTOS_DEST ='app/static/photos'
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alchemy:1012@localhost/tripi'
	SECRET_KEY = 'laziness'
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
	MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

	paypalrestsdk.configure({
		"mode": "sandbox",
		"client_id": "AT_VnbXIVNiMMSOCBdMBukGy1-sgdrEUp8Nc4b_4Gg0VoSsM2LbzUUFjnM9_lLl0vWhyQ5bEEIBehAQj",
		"client_secret": "ECuYlVhAGssqQLWNoafFxNxiXfacuPPfNbkt_xwDm_JvNWlZf2JBmSnmvGBAn8olJtkvhqiECXOUTWH8" })

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