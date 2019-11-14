from django.shortcuts import render
from django.views.generic import DetailView, FormView,ListView
from galery.models import GaleryModel
from galery.forms import GaleryForm

class HomePageView(ListView):
    model = GaleryModel
    template_name = 'galery/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['form'] = GaleryForm
        return context

    def post(self , request , *args , **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        print('ww')
        if form.is_valid():
            print('dd')
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class ImageFormViev(FormView):
    template_name = 'galery/home.html'

    form_class = GaleryForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super(ImageFormViev, self).form_valid(form)
