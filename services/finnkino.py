import requests
import xml.etree.ElementTree as ET

class FinnKinoXML(object):
    areas = {}
    area_url = "http://www.finnkino.fi/xml/TheatreAreas"
    schedule_url = "http://www.finnkino.fi/xml/Schedule/"
    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:43.0) Gecko/20100101 Firefox/43.0",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    }


    def get_area_codes(self):
		r = requests.get(self.area_url, headers=self.headers)
		root = ET.fromstring(r.content)
		areas = root.findall("TheatreArea")
		self._parse_areas(areas)
		return self.areas


    def _parse_areas(self, areas):
		for area in areas:
			id = area.find('ID').text
			name = area.find('Name').text
			self.areas[id] = name

    def get_movies_from_area(self, area_code):
    	url = "{}?area={}".format(self.schedule_url, area_code)
    	r = requests.get(url, headers=self.headers)
    	root = ET.fromstring(r.content)
    	shows = root.find('Shows').findall('Show')
    	return self._parse_shows(shows)

    def _parse_shows(self, shows):
    	movies = {}
    	for show in shows:
    		event_id = show.find('EventID').text
    		title = show.find('Title').text
    		rating = show.find('RatingImageUrl').text
    		genres = show.find('Genres').text.split(",")
    		movies[event_id] = {
    		    "title": title,
    		    "rating": rating,
    		    "genres": genres
    		}
    	return movies