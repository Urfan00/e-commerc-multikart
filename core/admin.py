from django.contrib import admin
from .models import Contact, Faq, OurTeam, Blog, Logo, InstaLogo, Subscribe, Employees


admin.site.register([Contact, Faq, OurTeam, Blog, Logo, InstaLogo, Subscribe, Employees])
