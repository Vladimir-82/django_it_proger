from django.shortcuts import render
from .models import Articles

# Create your views here.


def news_home(request):
    news = Articles.objects.order_by('-date')  # objects.all() получаем все объекты из модели models Articles
    return render(request, 'news/news_home.html', {'news': news})


