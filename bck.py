import phonenumbers
import opencage
import geopy
import geocoder
import folium

from numb import number


from phonenumbers import geocoder



pepnmber = phonenumbers.parse(number)

location = geocoder.description_for_number(pepnmber, "en")

print(location)



from phonenumbers import carrier

service_provider = phonenumbers.parse(number)

print(carrier.name_for_number(service_provider, "en"))




from opencage.geocoder import OpenCageGeocode

key = '0e8e998a63c64860b66682d820a29e3d'


geocoder = OpenCageGeocode(key)

query = str(location)

results = geocoder.geocode(query)
#print(results)




from geopy.geocoders import Nominatim


loc = Nominatim(user_agent="results")


getloc= loc.geocode("Mumbai")

print(getloc.address)




lat = getloc.latitude

lng = getloc.longitude

print(lat)
print(lng)






mymap = folium.Map(location= [lat, lng], zoom_start= 9)
folium.Marker([lat, lng], popup=location).add_to(mymap)



mymap.save("home.html")




