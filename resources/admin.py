from django.contrib import admin
from .models import UserProfile, Resource, ResourceRequest, RequestBoardPost

admin.site.register(UserProfile)
admin.site.register(Resource)
admin.site.register(ResourceRequest)
admin.site.register(RequestBoardPost)