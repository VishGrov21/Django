from django.contrib import admin
from first_proj.models import Topic, Webpage, AccessRecord

# Register your models here.

admin.site.register(Topic)
admin.site.register(AccessRecord)
admin.site.register(Webpage)
