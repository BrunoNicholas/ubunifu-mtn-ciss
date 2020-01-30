from system import app

APP_DEBUG   = True
APP_PORT    = 6000
APP_HOST    = '0.0.0.0'

if __name__ == '__main__':
	app.run(host=APP_HOST, port=APP_PORT, debug=APP_DEBUG)
	