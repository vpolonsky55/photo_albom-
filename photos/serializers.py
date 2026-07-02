# Сериализаторы — это классы в Django REST Framework.
# преобразуют данные (модели Django) в формат (JSON) и обратно.
from rest_framework import serializers
from .models import Photo, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = ['id', 'name', 'slug'] #Указываем, какие именно поля нужно включить в JSON. Только эти три поля будут отправлены в React
        # fields = '__all__'  # Все поля модели
        # exclude = ['created_at']  # Все поля, кроме created_at


class PhotoSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True) #по умолчанию было бы просто ID категорий, но заменяем его на вложенный сериализатор (Полные объекты категорий)
    image_url = serializers.SerializerMethodField() #кастомное поле, которое не существует в модели, но вычисляется "на лету". DRF видит поле image_url. Ищет метод get_image_url(self, obj)
    
    class Meta:
        model = Photo
        fields = [
            'id', 'image', 'image_url', 'title', 'description',
            'created_at', 'photo_date', 'categories'
        ]
    
    def get_image_url(self, obj): # obj — это экземпляр Photo
        # Метод для вычисления полного URL изображения
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url) #Это «умная» функция, которая превращает относительный путь в абсолютный URL, учитывая при этом домен и протокол, на котором висит твой сервер.
            return obj.image.url
        return None