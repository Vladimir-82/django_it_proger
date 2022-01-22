from django.shortcuts import render, redirect
from .models import Articles
from .forms import ActiclesForm
from django.views.generic import DetailView, UpdateView, DeleteView  # импортируем встроеный класс django для создания своего


def news_home(request):
    news = Articles.objects.order_by('-date')  # objects.all() получаем все объекты из модели models Articles
    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/detail_view.html'
    context_object_name = 'article'  # название ключа для передачи внутрь шаблона

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    # fields = ['title', 'anons', 'full_text', 'date']
    form_class = ActiclesForm  # работаем с классом ActiclesForm


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'  # куда идем после удаления статьи
    template_name = 'news/news-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ActiclesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была неверной'


    form = ActiclesForm() # работаем с классом ActiclesForm

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)


