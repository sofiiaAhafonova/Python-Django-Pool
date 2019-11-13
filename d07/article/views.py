from django.shortcuts import render
from django.views.generic import ListView, FormView, TemplateView,DetailView
from article.models import ArticleModel, UserFavoriteArticle
from django.contrib.auth.forms import AuthenticationForm
from article.forms import AddFavoriteArticleForm

class HomeView(TemplateView):
    model = ArticleModel
    template_name = "article/articles.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["user"] = self.request.user

class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "article/login.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context["user"] = self.request.user

class ArticleView(ListView):
    model = ArticleModel
    template_name = "article/articles.html"

    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        context["user"] = self.request.user

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