from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics, filters

from .models import Articles
from .forms import ActiclesForm
from .serializers import Articles_serializer



def news_home(request):
    news = Articles.objects.all()
    return render(request, 'news/news_home.html', {'news': news, 'count': news.count()})

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
    # fields = ['title', 'anons', 'full_text', 'date']
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


# class APIArticles(APIView):
#     def get(self, request):
#         articles = Articles.objects.all()
#         serializer = Articles_serializer(articles, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = Articles_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class APIArticles(generics.ListCreateAPIView):
    queryset = Articles.objects.all()
    serializer_class = Articles_serializer


class APISearch(generics.ListAPIView):
    queryset = Articles.objects.all()
    serializer_class = Articles_serializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'anons', 'full_text',]


class APIArticlesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articles.objects.all()
    serializer_class = Articles_serializer






