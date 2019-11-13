from django.db import models
from django.contrib.auth.models import User

class ArticleModel(models.Model):
    title = models.CharField(max_length = 64, null = False)
    author = models.ForeignKey(User, null = False,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, null = False)
    synopsis = models.CharField(max_length = 312, null = False)
    content = models.TextField(null = False)

    class Meta:
        db_table = 'articles'

    def __str__(self):
        return self.title

class UserFavouriteArticle(models.Model):
    user = models.ForeignKey(User, null = False, on_delete=models.CASCADE)
    article = models.ForeignKey(ArticleModel, null = False, on_delete=models.CASCADE)

    def __str__(self):
        return self.article.title
