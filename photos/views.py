# generics Готовые классы для CRUD-операций (создание, чтение, обновление, удаление)
# filters Фильтрация, поиск, сортировка
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend  #Фильтрация по полям модели (categories__slug)
from .models import Photo, Category
from .serializers import PhotoSerializer, CategorySerializer

#список и создание фото
class PhotoListAPIView(generics.ListCreateAPIView): #ListCreateAPIView — даёт 2 метода: (GET /api/photos/ → список всех фото), (POST /api/photos/ → создать новое фото)
    """Список фотографий с фильтрацией по категориям"""
    queryset = Photo.objects.all().prefetch_related('categories') #Загружаем категории сразу. Чтобы не делать лишние запросы в базу.
    serializer_class = PhotoSerializer #Превращаем в JSON
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter] #Какие инструменты фильтрации доступны, Чтобы React мог фильтровать данные
    filterset_fields = ['categories__slug'] #По каким полям фильтровать. ?categories__slug=nature
    search_fields = ['title', 'description'] #По каким полям искать ?search=закат
    ordering_fields = ['photo_date', 'created_at'] #По каким полям сортировать	?ordering=created_at
    ordering = ['photo_date'] #Сортировка по умолчанию. Новые фото сверху (минус = по убыванию)

# детали, обновление, удаление
class PhotoDetailAPIView(generics.RetrieveUpdateDestroyAPIView): #RetrieveUpdateDestroyAPIView — даёт 3 метода: (GET /api/photos/1/ → получить одно фото), (PUT /api/photos/1/ → обновить фото), (DELETE /api/photos/1/ → удалить фото)
    """Детальная информация о фотографии"""
    queryset = Photo.objects.all().prefetch_related('categories') # look up
    serializer_class = PhotoSerializer # look up


class CategoryListAPIView(generics.ListAPIView): #ListAPIView — даёт 1 метод: (GET /api/categories/ → список всех категорий)
    """Список всех категорий"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter] #Можно искать по названию
    search_fields = ['name'] #Искать по полю name