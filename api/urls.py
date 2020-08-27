from django.urls import path

from .views import ArticleAPIView , ListArticle , DetailArticle



urlpatterns = [
    path("",ArticleAPIView.as_view()),
    path("<int:pk>/",DetailArticle.as_view()),
    path("<int:pk>/", ListArticle.as_view()),
    
]