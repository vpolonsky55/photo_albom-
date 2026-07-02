from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
    """Модель категории"""
    name = models.CharField('Название', max_length=100, unique=True)
    slug = models.SlugField('URL-метка', max_length=100, unique=True)
    # created_at УДАЛЁН

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Photo(models.Model):
    """Модель фотографии"""
    image = models.ImageField('Изображение', upload_to='', null=True, blank=True)
    title = models.CharField('Заголовок', max_length=200, blank=True)
    description = models.TextField('Описание', blank=True)
    created_at = models.DateTimeField('Дата создания карточки', auto_now_add=True)
    photo_date = models.DateTimeField(
        'Дата съёмки',
        null=True,
        blank=True,
        help_text='Укажите дату и время, когда была сделана фотография'
    )
    categories = models.ManyToManyField(
        Category,
        related_name='photos',
        verbose_name='Категории',
        blank=True
    )

    def __str__(self):
        return self.title or f'Фото #{self.id}'

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['-created_at']