import phonenumbers
import folium
from folium import Map

number = "+966536896780"
from phonenumbers import geocoder
ch_number = phonenumbers.parse(number, "CH")
yourLocation = geocoder.description_for_number(ch_number, "en")
from phonenumbers import carrier
service_provider = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key='18d46ff0346a48bdab8edb710cfab1ad')

query = str(yourLocation)

results = geocoder.geocode(query)
print(results)

Lat = results[0]['geometry']['lat']
Lng = results[0]['geometry']['lng']

print(Lat,Lng)

myMap = folium, Map