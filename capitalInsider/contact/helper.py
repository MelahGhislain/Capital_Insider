from django.contrib.gis.geoip2 import  GeoIP2

# Helper functions

def get_geo(ip):
    g = GeoIP2()
    country = g.country(ip)
    city = g.city(ip)
    lat, lon = g.lat_lon(ip)
    return country, city, lat, lon

def get_center_coordinate(latA, lonA, latB=None, lonB=None):
    cord = (latA, lonB)
    if latB:
        cord = [(latA+latB)/2, (lonA+lonB)/2]
    return cord

def get_zoom(distance):
    if distance <= 100:
        return 8
    elif distance > 100 and distance <= 5000:
        return 4
    else:
        return 2

