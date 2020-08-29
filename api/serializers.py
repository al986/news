from rest_framework import serializers

from articles.models import Article

from users.models import CustomUser

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title","body",)


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("username","email",)



        
                      