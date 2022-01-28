from django.forms import ModelForm
from django.forms import ClearableFileInput
from . import models

class CreateTokoForm(ModelForm):
	class Meta:
		model=models.Toko
		exclude=['pemilik']