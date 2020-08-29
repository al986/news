from rest_framework import generics 

from articles.models import Article 
from users.models import CustomUser

from .serializers import ArticleSerializer
from .serializers import CustomUserSerializer

# Create your views here.
class ArticleAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ListArticle(generics.ListAPIView):
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

   
