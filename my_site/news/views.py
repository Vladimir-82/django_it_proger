from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from django.db.models import Q



from rest_framework import generics, filters, permissions

from .models import Articles, Category
from .forms import ActiclesForm
from .serializers import Articles_serializer
from .permissions import IsAuthorOrReadOnly



def news_home(request):
    news = Articles.objects.all()
    return render(request, 'news/news_home.html', {'news': news, 'count': news.count()})

def category(request, category_id):
    article = Articles.objects.filter(category=category_id)
    current_category = Category.objects.get(pk=category_id)
    context = {'article': article, 'current_category': current_category,
               'count': article.count()}
    return render(request, 'news/categories.html', context)


def list_categories(request):
    categories = Category.objects.all()
    context = {'categories': categories, 'count': categories.count()}
    return render(request, 'news/list_categories.html', context)


def category(request, category_id):
    article = Articles.objects.filter(category=category_id)
    categories = Category.objects.all()
    preview = category_id - 1
    if preview < 1:
        preview = categories.count()
    next = category_id + 1
    if next > categories.count():
        next = 1
    current_category = Category.objects.get(pk=category_id)
    context = {'article': article, 'categories': categories,
               'current_category': current_category, 'count': article.count(), 'preview': preview, 'next': next}
    return render(request, 'news/categories.html', context)


def search(request):
    query = request.GET.get('q')
    content = Articles.objects.filter(Q(title__contains=query) | Q(anons__contains=query) | Q (full_text__contains=query))
    return render(request, 'news/search.html', {'search': content, 'count': content.count()})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/detail_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ActiclesForm
    success_url = '/news/'


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
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


    form = ActiclesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)


class APIArticlesGet(generics.ListAPIView):
    queryset = Articles.objects.all()
    serializer_class = Articles_serializer

class APIArticlesPost(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Articles.objects.all()
    serializer_class = Articles_serializer




class APISearch(generics.ListAPIView):
    queryset = Articles.objects.all()
    serializer_class = Articles_serializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'anons', 'full_text',]


class APIArticlesDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Articles.objects.all()
    serializer_class = Articles_serializer