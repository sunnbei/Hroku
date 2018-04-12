from django.contrib import admin
from .models import Members,Bands,Seasons

# Register your models here.
admin.site.register(Members)

admin.site.register(Bands)

admin.site.register(Seasons)