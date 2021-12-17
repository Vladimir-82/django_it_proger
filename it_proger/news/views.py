from django.shortcuts import render, redirect
from .models import Articles
from .forms import ActiclesForm
from django.views.generic import DetailView # импортируем встроеный класс django для создания своего

# Create your views here.


def news_home(request):
    news = Articles.objects.order_by('-date')  # objects.all() получаем все объекты из модели models Articles
    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/detail_view.html'
    context_object_name = 'article' # название ключа для передачи внутрь шаблона


def create(request):
    error = ''
    if request.method == 'POST':
        form = ActiclesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была неверной'


    form = ActiclesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)


