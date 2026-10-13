from django.contrib import admin
from .models import Editorial, Libro

@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais', 'fundacion')
    list_filter = ('pais',)
    search_fields = ('nombre', 'pais')

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editorial', 'autor', 'stock', 'formatted_precio')
    list_filter = ('editorial', 'stock')
    search_fields = ('titulo', 'autor')

    @admin.display(description='Precio')
    def formatted_precio(self, obj):
        return f"${obj.precio:,.0f}".replace(',', '.')