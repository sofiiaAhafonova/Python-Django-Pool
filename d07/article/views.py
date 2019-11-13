from django.shortcuts import render
from django.views.generic import ListView, FormView, TemplateView
from article.models import ArticleModel
from django.contrib.auth.forms import AuthenticationForm


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
