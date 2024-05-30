from django.contrib import admin

# Register your models here.
from .models import Klass, Hotel, Travel

admin.site.register(Klass)
admin.site.register(Hotel)
admin.site.register(Travel)
