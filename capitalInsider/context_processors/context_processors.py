from datetime import datetime
from services.models import Services
from contact.models import ContactInfo, SocialNetwork


def services_context_processor(request):
    services = Services.objects.all()#[:6]
    titles = map(lambda service: {"id": service.id,
                 "title":  service.title}, services)
    return {
        "titles": titles,
    }


def contact_info_context_processor(request):
    contact_info = ContactInfo.objects.all()#[0]
    social_icons = SocialNetwork.objects.all()

    return {
        "contact_info": contact_info,
        "social_icons": social_icons
    }


def current_year_context_processor(request):
    current_datetime = datetime.now()
    return {
        'current_year': current_datetime.year,
    }
