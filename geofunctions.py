import geocoder
import json

f = open('Google_API/client_secret.json')
keys = json.load(f)

def get_coordinates(address):
    try:
        location = geocoder.google(address, key=keys['private_key_id'])
    except:
        print("Geocoder failed")
    if location is None:
        print("Error to get coordinates of " + address)
        return
    return [location.latlng[0], location.latlng[1]]

def get_addresses(streets):  #list of addresses, list of cities
    addresses = [str(address)+' Pamplona' for address in streets]
    return addresses

def addresses_to_coordinates(addresses):
    coordinates = []
    for address in addresses:
        coordinates.append(get_coordinates(address))
    return coordinates