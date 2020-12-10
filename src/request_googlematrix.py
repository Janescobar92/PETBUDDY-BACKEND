import requests
from models import db, User, Animals, Services, Operations, Service_type

api_key = "AIzaSyB0Z-gx11fiLL1MG9fO7zVsUWGHoacTgKM"

matrix_url = "https://maps.googleapis.com/maps/api/distancematrix/json?"

def destiny(id_user, service_type_id):
    origin_location = User.get_origin(id_user)
    destiny_location = Services.all_service_destinations(service_type_id)
    # print (origin_location, origin_location)

    origin_address = origin_location["address"]

    mode = "&mode=walking&language=es&key="
    varOr = "origins=" +  origin_address
    result = []
    for eachdestiny in destiny_location:
        distance_service = {}
        varDest = "&destinations="+ eachdestiny["address"]
        r = requests.get( matrix_url + varOr + varDest + mode + api_key)
        distance = r.json()["rows"][0]["elements"][0]["distance"]["text"]
        distance_service = {"id_user_offer": eachdestiny["id"], "distance": distance}
        result.append(distance_service)

    return result