from django.contrib import admin
from .models import Book,Category

class BookAdmin(admin.ModelAdmin):
    list_display = ('name','author','price')

admin.site.register(Book,BookAdmin)
admin.site.register(Category)

