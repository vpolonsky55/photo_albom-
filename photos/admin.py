from django.contrib import admin
from .models import Photo, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'photo_date', 'image_preview')
    # list_filter = ('categories', 'created_at', 'photo_date')
    list_filter = ('categories', ) #Добавляет боковую панель с фильтрами
    search_fields = ('title', 'description') #Добавляет поле поиска вверху страницы
    filter_horizontal = ('categories',) # удобное представление фильтров внутри карточки. Выбор ManyToMany
    readonly_fields = ('created_at',)
    list_display_links = ('title',) # Указывает, по каким колонкам можно кликнуть для перехода к редактированию
    
    # Группирует поля в логические блоки
    fieldsets = (
        ('Основное', {
            'fields': ('image', 'title', 'description')
        }),
        ('Даты', {
            'fields': ('created_at', 'photo_date')
        }),
        ('Категории', {
            'fields': ('categories',)
        }),
    )
    
    def image_preview(self, obj):
        if obj.image:
            from django.utils.html import mark_safe
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" style="object-fit:cover;border-radius:4px;" />')
        return '—'
    image_preview.short_description = 'Превью'