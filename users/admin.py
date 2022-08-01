from django.contrib import admin

# Register your models here.


from users.models import User, Seller, Buyer


admin.site.register(User)
admin.site.register(Seller)
admin.site.register(Buyer)


