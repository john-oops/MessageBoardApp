from django.contrib import admin

# Register your models here.
from .models import Post # регестрация приложения
admin.site.register(Post)