from django.db import models



class Articles(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    anons = models.CharField(max_length=150, verbose_name='Анонс')
    full_text = models.TextField(verbose_name='Статья')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Категория')

    def __str__(self):
        return f'Новость: {self.title}'

    def get_absolute_url(self):
        return f'/news/{self.pk}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-date', 'title']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']