from django.contrib import admin
from myapp.models import Product,User
# Register your models here.

# simple way to regiester
# admin.site.register(Product)
# admin.site.register(User)

# cleaner approach to register using @admin.register
@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["name","age","email","is_paid","date_of_purchase"]
    search_fields = ["name","is_paid"]
    list_filter = ["is_paid"]

    