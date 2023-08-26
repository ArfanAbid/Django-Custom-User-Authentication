from django.contrib import admin
from Authentication.models import CustomUser
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'is_active', 'last_login', 'date_joined')
    
    
    
    list_filter = ('first_name', 'id', 'is_active')  # `list_filter` is a property of the `CustomUserAdmin` class that specifies which fields should be displayed as filters in the admin interface. In this case, the filters will be based on the `first_name`, `id`, and `is_active` fields of the `CustomUser` model. 

    search_fields = ('email', 'first_name') # The `search_fields` attribute in the `CustomUserAdmin` class is used to specify the fields that can be searched in the admin interface. In this case, the `email` and `first_name` fields of the`CustomUser` model can be searched.
    
    ordering = ('email',)
    
admin.site.register(CustomUser,CustomUserAdmin)    
    