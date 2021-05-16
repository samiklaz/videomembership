from django.contrib import admin
from .models import Membership, UserMemberships, Subscription

admin.site.register(Membership)
admin.site.register(UserMemberships)
admin.site.register(Subscription)
