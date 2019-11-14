from django.forms import ModelForm
from galery.models import GaleryModel

class GaleryForm(ModelForm):
     class Meta:
        model = GaleryModel
        fields = ['image', 'title']
