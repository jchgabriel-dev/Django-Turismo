from django import forms
from travello.models import Destination

class PlacesForm(forms.ModelForm):
	class Meta:
		model = Destination
		fields = [
		'name',
		'img',
		'desc',
		'price',
		'offer',
		]

class Places(forms.Form):
	name = forms.CharField(label='Name', max_length=20)
	img = forms.ImageField(label='Image')
	desc = forms.CharField(
		label='Description',
		widget = forms.Textarea(
				attrs={
					'class':'special',
					'cols':'10',
				}
			)
		)
	price = forms.IntegerField(label='Price', min_value=0, max_value=1000000)
	offer = forms.BooleanField(required=False, label='Offer')