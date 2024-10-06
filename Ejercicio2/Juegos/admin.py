from django.contrib import admin

# Register your models here.
from .models import Shooter
admin.site.register(Shooter)

from .models import Rogelite
admin.site.register(Rogelite)

from .models import Soulslike
admin.site.register(Soulslike)

