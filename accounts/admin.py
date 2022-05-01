from django.contrib import admin
from .models import  CustomUser,DoctorsTable,CategoryTable,AppointMail
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(DoctorsTable)
admin.site.register(CategoryTable)
admin.site.register(AppointMail)