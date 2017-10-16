from django.contrib import admin
import models

from .models import Post
admin.site.register(Post)
