from django.contrib import admin
from .models import Tags, Donor, Post
# Register your models here.

admin.site.register(Tags)
admin.site.register(Donor)
admin.site.register(Post)