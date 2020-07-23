from django.contrib import admin

# Register your models here.
from .models import Item


# admin에 item 노출되도록
# admin.site.register(Item)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'short_desc', 'price', 'is_publish']
    list_display_links = ['name']
    list_filter = ['is_publish', 'updated_at']
    search_fields = ['name']


    def short_desc(self, item):  # Item에서 가져온 하나의 객체
        return item.desc[:20]
