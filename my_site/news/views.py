from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView  # импортируем встроеный класс django для создания своего
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics

from .models import Articles
from .forms import ActiclesForm
from .serializers import Articles_serializer



def news_home(request):
    news = Articles.objects.all()  # order_by('-date') получаем сортировку. Но у меня  прямо в моделе
    search = Articles.objects.filter(title__contains='skills')
    return render(request, 'news/news_home.html', {'news': news, 'search': search})

def search(request):
    if (request.method == 'GET'):
        response = request.GET.get('response', False)
        search = Articles.objects.filter(title__contains=response)
    return render(request, 'news/news_home.html', {'search': search})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/detail_view.html'
    context_object_name = 'article'  # название ключа для передачи внутрь шаблона

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    # fields = ['title', 'anons', 'full_text', 'date']
    form_class = ActiclesForm  # работаем с классом ActiclesForm
    success_url = '/news/'


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


class APIArticlesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articles.objects.all()
    serializer_class = Articles_serializer


