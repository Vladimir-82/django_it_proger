from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('search', views.search, name='search'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete'),
    path('api/news/', views.APIArticles.as_view()),
    path('api/search/', views.APISearch.as_view()),
    path('api/news/<int:pk>', views.APIArticlesDetail.as_view()),
    ]