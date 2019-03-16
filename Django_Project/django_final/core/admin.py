from django.contrib import admin
from .models import Owner, Repos

# Register your models here.
admin.site.register(Owner)
admin.site.register(Repos)
