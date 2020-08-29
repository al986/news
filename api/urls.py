from django.urls import path

from .views import (
    ArticleAPIView ,
    ListArticle , 
    DetailArticle,
    ListCustomUser,
    DetailCustomUser,
)
    



urlpatterns = [
    path("",ArticleAPIView.as_view()),
    path("<int:pk>/", ListArticle.as_view()),
    path("<int:pk>/",DetailArticle.as_view()),
    path("<int:pk>/", ListCustomUser.as_view()),
    path("<int:pk>/",DetailCustomUser.as_view()),
    
    
]