from django.contrib import admin
from .models import Profile,Student,Course,Professor,Class

admin.site.register(Profile)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Professor)
admin.site.register(Class)

# Register your models here.
