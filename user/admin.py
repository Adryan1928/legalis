from django.contrib import admin
from .models import Client, Course, Enrollment

admin.site.register(Client)
admin.site.register(Course)
admin.site.register(Enrollment)
