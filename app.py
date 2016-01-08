from flask import Flask, render_template
from services.finnkino import FinnKinoXML
app = Flask(__name__)
fk = FinnKinoXML()
@app.route('/')
def index():
	#return 'Hello World!'
	areas = fk.get_area_codes()
	data = {
		'areas': areas
	}
	return render_template('index.html', data=data)

if __name__ == "__main__":
	app.run()