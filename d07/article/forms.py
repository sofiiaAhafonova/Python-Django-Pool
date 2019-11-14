from django.forms import forms
from django.forms import ModelForm
from article.models import ArticleModel

class AddFavoriteArticleForm(forms.Form):
    pass


class ArticleForm(ModelForm):
     class Meta:
         model = ArticleModel
         fields = ['title', 'synopsis', 'content', ]

