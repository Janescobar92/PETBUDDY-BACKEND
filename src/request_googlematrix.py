import requests

#  API KEY
api_key = "AIzaSyB0Z-gx11fiLL1MG9fO7zVsUWGHoacTgKM"

# from where
myLocation = "Madrid+ON|95+calle+lagasca+mMadrid+ON"
# origins=Bobcaygeon+ON|24+Sussex+Drive+Ottawa+ON   address example
# origins=Madrid+ON|95+calle+lagasca+mMdrid+ON   address example

# To where
destination = "Sanlorenzodeelescorial+ON|7+calle+jacometrezo+mMadrid+ON"

# base URL 
matrix_url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + myLocation + "&destinations="+ destination +"&mode=walking&language=es-FR&key="
# outputFormat?parameters

# r = requests.get(matrix_url + myLocation + "&destinations=" + destination + "&key="+ api_key)
r = requests.get( matrix_url+ api_key)

# return 
distance = r.json()
# return just the distance between the origin and destination
# distance = r.json()["rows"][0]["elements"][0]["distance"]["text"]