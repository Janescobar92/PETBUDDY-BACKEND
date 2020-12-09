# import requests
# from main.py import varOR, varDest

# #  API KEY
# api_key = "AIzaSyB0Z-gx11fiLL1MG9fO7zVsUWGHoacTgKM"

# # from where
# # myLocation = "origins=Madrid+ON|95+calle+lagasca+Madrid+ON"
# # myLocation = "origins=" 
# # origins=Bobcaygeon+ON|24+Sussex+Drive+Ottawa+ON   address example
# # origins=Madrid+ON|95+calle+lagasca+mMdrid+ON   address example

# # To where
# # destination = "&destinations="

# # Travel mode + api_key filter
# matrix_url = "https://maps.googleapis.com/maps/api/distancematrix/json?"

# mode = "&mode=walking&language=es&key="


# def destiny(myLocation, destination):
# r = requests.get( matrix_url + myLocation + destination + mode + api_key)
#     # r = requests.get( matrix_url + myLocation + destination + mode + api_key)
# distance = r.json()["rows"][0]["elements"][0]["distance"]["text"]
#     # return distance

# # base URL 
# matrix_url + outputFormat?parameters

# r = requests.get(matrix_url + myLocation + "&destinations=" + destination + "&key="+ api_key)

    # distance = r.json()
# return full object
# return just the distance between the origin and destination