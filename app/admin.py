from django.contrib import admin
from app.models import User, Complaint
# Register your models here.

admin.site.register(User)
admin.site.register(Complaint)
# admin.site.register(Post, MarkdownModelAdmin)