
from django.test import TestCase
from .models import Article
from .models import CustomUser
# Create your tests here.

class ArticleModelTest (TestCase):
    @classmethod
    def setUpTestData(cls):
        Article.object.Create (title="frist article", body =" a body here")

    def test_title_content(self):
        article = Article.object.get(id=1)
        expected_object_name = f"{article.title}"
        self.assertEquals(expected_object_name, "frist article")

    def test_body_content(self):
        article = Article.object.get(id=1)
        expected_object_name = f"{article.body}"
        self.assertEquals(expected_object_name, "a body here")



 
class CustomUserModelTest (TestCase):
    @classmethod
    def setUpTestData(cls):
        CustomUser.object.Create( username="your name", email =" your e-mail")

    def test_username_content(self):
        users = CustomUser.object.get(id=2)
        expected_object_name = f"{users.CustomUser}"
        self.assertEquals(expected_object_name, "your name")

    def test_email_content(self):
        users = CustomUser.object.get(id=2)
        expected_object_name = f"{users.email}"
        self.assertEquals(expected_object_name, "your e-mail") 
       