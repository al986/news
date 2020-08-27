
from django.test import TestCase
from .models import Article
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