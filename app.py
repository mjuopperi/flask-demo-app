from flask import Flask, render_template
from services.finnkino import FinnKinoXML
from services.leffatykki import LeffaTykkiRSS
app = Flask(__name__)
fk = FinnKinoXML()
lt = LeffaTykkiRSS()

def get_movies_with_reviews(area_code):
	movie_container = {}
	movies = fk.get_movies_from_area(area_code)
	reviews = lt.get_movie_reviews()
	for id, movie in movies.iteritems():
		review_link = ""
		title = movie['title']
		if title in reviews:
			review_link = reviews[movie['title']]
		movie_container[id] = {
			'title': movie['title'],
			'rating': movie['rating'],
			'genres': "".join(movie['genres']),
			'review': review_link
		}
	return movie_container

@app.route('/')
def index():
	#return 'Hello World!'
	areas = fk.get_area_codes()
	movies = get_movies_with_reviews(1033)
	data = {
		'areas': areas,
		'movies': movies
	}
	return render_template('index.html', data=data)

if __name__ == "__main__":
	app.run()