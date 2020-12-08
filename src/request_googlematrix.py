import requests

#  API KEY
api_key = "AIzaSyB0Z-gx11fiLL1MG9fO7zVsUWGHoacTgKM"

# from where
myLocation = "Madrid,spain"

# To where
destination = "Barcelona,spain"

# base URL 
matrix_url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + myLocation + "&destinations="+ destination +"&mode=walking&language=es-FR&key="
# outputFormat?parameters

# r = requests.get(matrix_url + myLocation + "&destinations=" + destination + "&key="+ api_key)
r = requests.get( matrix_url+ api_key)

# return 
distance = r.json()