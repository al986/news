from  django.urls import path
from django.urls import path
from django.views import ListArticle, ArticleUpdateView, ArticleDeleteView, DetailArticle, ArticleCreateView

from django.views import(
    ListArticle,
    ArticleUpdateView,
    ArticleDeleteView,
    DetailArticle,
    ArticleCreateView, ListCustomUser,
    DetailCustomUser,
)
from rest_framework.routers import SimpleRouter

    



urlpatterns = [
    path("users/", ListCustomUser.as_view()),
    path("users/<int:pk>/", DetailCustomUser.as_view()),
    path("<int:pk>/edit/", ArticleUpdateView.as_view(), name="article_edit"),
    path("<int:pk>/", DetailArticle.as_view(), name="article_detail"),
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),
]