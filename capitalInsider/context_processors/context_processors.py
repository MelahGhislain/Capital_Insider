from datetime import datetime
from services.models import Services
from contact.models import ContactInfo, SocialNetwork
from projects.models import Projects


def services_context_processor(request):
    services = Services.objects.all()#[:6]
    titles = map(lambda service: {"id": service.id,
                 "title":  service.title}, services)
    return {
        "titles": titles,
    }
def projects_context_processor(request):
    return {
        "ifProject": True if Projects.objects.all() else False
    }


def contact_info_context_processor(request):
    contact_info = ContactInfo.objects.first()#[0]
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
