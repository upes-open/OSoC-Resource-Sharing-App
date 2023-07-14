from django.contrib import admin

from discussions.models import Discussion, Comment,Resource

admin.site.register(Discussion)
admin.site.register(Comment)
admin.site.register(Resource)