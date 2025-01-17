from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Product, Category, CustomUser


# Admin configuration for Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')  # Fields to display in the list view
    search_fields = ('name',)  # Search by name
    list_filter = ('created_at', 'updated_at')  # Add filter options


# Admin configuration for Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock_quantity', 'created_at')  # Fields to display
    search_fields = ('name', 'category__name')  # Allow search by product and category names
    list_filter = ('category', 'created_at')  # Filter by category and creation date


# Admin configuration for CustomUser
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active')  # Fields to display in the admin list view
    list_filter = ('is_staff', 'is_active')  # Add filters for staff and active status
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


# Register models with their respective admin classes
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(CustomUser, CustomUserAdmin)