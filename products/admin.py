from django.contrib import admin

# Register your models here.
from products.models import Flowers, ReviewForProduct, ReviewForSeller

admin.site.register(Flowers)
admin.site.register(ReviewForProduct)
admin.site.register(ReviewForSeller)