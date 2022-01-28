from django.forms import ModelForm
from . import models

class SalesForm(ModelForm):
    class Meta:
        model = models.Sale
        exclude=['owner']

    def __init__(self, *args, **kwargs):
        super(SalesForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['class'] = 'form-control'
        

class SaleDetail(ModelForm):
    class Meta:
        model = models.SaleDetail
        exclude=['owner','sale', 'toko', 'resi','kode_t',]
        







