from django.contrib import admin
from .models import Articles, Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'anons', 'full_text', 'date', 'category')
    list_display_links = ('title', 'date', 'category')
    search_fields = ('title', 'date', 'category')

admin.site.register(Articles, NewsAdmin)
admin.site.register(Category)

