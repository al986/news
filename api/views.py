from articles.models import Article
from rest_framework import viewsets
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from users.models import CustomUser
from .serializers import ArticleSerializer
from .serializers import CustomUserSerializer
from rest_framework import generics



# Create your views here.
class ArticleAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class DetailArticle (generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
###########


class ListCustomUser(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class DetailCustomUser (generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer



class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"

   
