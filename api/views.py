from rest_framework import generics

from articles.models import Article 


from .serializers import ArticleSerializer

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
