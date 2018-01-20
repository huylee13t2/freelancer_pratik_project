from django.contrib import admin
from app.models import Account, Locality, Society, City, PropertyType


admin.site.register(Account)
admin.site.register(City)
admin.site.register(Locality)
admin.site.register(Society)
admin.site.register(PropertyType)
