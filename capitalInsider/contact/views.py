from django.shortcuts import render
from .models import FinancialAdvisor, ContactInfo, SocialNetwork
from .forms import ContactForm, MapForm
from django.views import View
from django.http import  HttpResponseRedirect
from django.core.mail import  send_mail
from geopy.geocoders import Nominatim
from geopy.distance import  geodesic
from .helper import get_geo, get_center_coordinate, get_zoom
import folium

# Create your views here.
class ContactView(View):
    def get(self, request):
        advisors = FinancialAdvisor.objects.all()
        contact = ContactInfo.objects.last()
        social_networks = SocialNetwork.objects.all()

        form = ContactForm()
        map_form = MapForm()

        ######################################################
        geolocator = Nominatim(user_agent="contact")
        ip = '195.24.220.35'
        country, city, lat, lon = get_geo(ip)
        # location = geolocator.geocode(city)
        destination = geolocator.geocode(city)

        # destination coordinates
        d_lat = lat
        d_lon = lon

        pointA = get_center_coordinate(d_lat, d_lon)
            # initial folium map
        m = folium.Map(width=1290, height=500, destination=pointA, zoom_start=13)
        folium.Marker([ d_lat, d_lon], tooltip="Capital Insider", popup=city['city'], icon=folium.Icon(color="red")).add_to(m)
        
        n = m._repr_html_()
        ##################################################################

        return render(request, "contact/index.html", {
            "advisors": advisors,
            "contact": contact,
            "socials": social_networks,
            "form": form,
            "map_form": map_form,
            "map": n,
        })

    def post(self, request):
        form = ContactForm(request.POST)
        map_form = MapForm(request.POST)
        #######################################################################
        geolocator = Nominatim(user_agent="contact")
        ip = '72.14.207.99'
        country, city, lat, lon = get_geo(ip)
        # location = geolocator.geocode(city)
        destination = geolocator.geocode(city)

        # destination coordinates
        d_lat = lat
        d_lon = lon

        pointA = (d_lat, d_lon)

       
        ####################################################################
        if form.is_valid():
            username = form.cleaned_data['user_name']
            email = form.cleaned_data['email']
            # number = form.cleaned_data['phone_num']
            message = form.cleaned_data['message']
            send_mail(
                username, # subject
                message, # message
                email, # from email
                ["melahghislain17@gmail.com"], # to email
            )
            
            return HttpResponseRedirect("/contact")
        if map_form.is_valid():
            instance = map_form.save(commit=False)
            # _destination = map_form.cleaned_data.get('destination')
            # destination = geolocator.geocode(_destination)
            # d_lat = destination.latitude
            # d_lon = destination.longitude
            _location = map_form.cleaned_data.get('location')
            location = geolocator.geocode(_location)
            # laction coordinates
            l_lat = location.latitude
            l_lon = location.longitude
            pointB = (l_lat, l_lon)
            distance = round(geodesic(pointA, pointB).km, 2)
            cord = get_center_coordinate(d_lat, d_lon, l_lat, l_lon)
            # folium map modification
            m = folium.Map(width=1600, height=800, destination=cord, zoom_start=get_zoom(distance))
            # destination marker
            folium.Marker([ d_lat, d_lon], tooltip="Capital Insider", popup=city['city'], icon=folium.Icon(color="red")).add_to(m)
            # laction marker
            folium.Marker([ l_lat, l_lon], tooltip="Capital Insider", popup=location, icon=folium.Icon(color="purple", icon='cloud')).add_to(m)
            # draw line between location and destinstion\
            line = folium.PolyLine(locations=[pointA, pointB], weight=5, color="blue",)
            m.add_child(line)
            n = m._repr_html_()

            # instance.location = location
            instance.destination = destination
            instance.distance = distance
            instance.save()
            
            return HttpResponseRedirect("/contact")

        advisors = FinancialAdvisor.objects.all()
        contact = ContactInfo.objects.last()
        social_networks = SocialNetwork.objects.all()

        return render(request, "contact/index.html", {
            "advisors": advisors,
            "contact": contact,
            "socials": social_networks,
            "form": form,
            "map_form": map_form,
            "map": n,
        })

