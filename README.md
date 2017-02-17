# umw-goats
DE Hack U 5 Student Repository

## Installation

The code can be installed from github.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Usage
### Basics

The program uses API to provide readable information to the user, using a Heroku instance.
The program imports and uses API from, Yelp, Zillow, Your Mapper Crime Score, and Google.

To use the sample of the program input a zip code search, the program will return to you the ability to see what restraunts are in that area, what shops, houses, nightlife, attractions and the crime rates of the area. 

The GUI will display a actively updating map for traffic and will display heat maps for crime. It will display pinpoints for restraunts and the like. There are active buttons to manuver between the display categories. The GUI also has an overall quality of life for the area. 

### Yelp API

https://github.com/Yelp/yelp-python

The Yelp API and its Search Class and Businesses Class have been added to contribute to providing information on restraunts, shops, activities, and nightlife. 

### PyZillow API

https://pypi.python.org/pypi/pyzillow/0.5.5

The Python wrapped Zillow API is being used to provide relevant information on houses. 

### Google Maps Static Maps API

The Goggle Maps Static Maps API has been added to provide a image of the map to the GUI

### Your Mapper Crime Score API

The Crime Score API is an add-on to the Google API  and provides pinpoints of the location and type of crimes in the area. 


