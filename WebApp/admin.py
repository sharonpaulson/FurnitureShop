from django.contrib import admin
from WebApp.models import SignupDB, CartDB, OrderDB, ContactDB

admin.site.register(SignupDB)
admin.site.register(CartDB)
admin.site.register(OrderDB)
admin.site.register(ContactDB)
