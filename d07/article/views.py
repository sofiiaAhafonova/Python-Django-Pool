from django.shortcuts import render
from django.views.generic import ListView, FormView, TemplateView,DetailView, RedirectView
from article.models import ArticleModel, UserFavoriteArticle
from django.contrib.auth.forms import AuthenticationForm
from article.forms import AddFavoriteArticleForm, ArticleForm

class HomeView(ListView):
    model = ArticleModel
    template_name = "article/articles.html"

class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "article/login.html"
    success_url = "/"


class ArticleView(ListView):
    model = ArticleModel
    template_name = "article/articles.html"


class PublicationsView(ListView):
    model = ArticleModel
    template_name = "article/publications.html"


class ArticleDetailView(DetailView):
    model = ArticleModel
    template_name = "article/detail.html"
    
    
class FavoritesView(ListView):
    model = UserFavoriteArticle
    template_name = "article/favorites.html"

class AddFavoriteView(FormView):
    form_class = AddFavoriteArticleForm
    template_name = "article/detail.html"
    success_url = "/"

class PublishView(FormView):
    form_class = ArticleForm
    template_name = "article/publish.html"
    success_url = "/"

    def form_valid(self, form):
        item = form.save(commit=False)
        item.author = self.request.user
        item.save()
        return super().form_valid(form)

