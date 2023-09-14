from django.contrib import admin
from . models import Post, Comment, Rating, User


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(User)
