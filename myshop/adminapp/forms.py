from django import forms
from django.contrib.auth.forms import UserChangeForm
from mainapp.models import Product, Category
from authapp.models import ShopUser

class UserForm(forms.ModelForm):

	class Meta:
		model = ShopUser
		fields = ('username', 'first_name', 'email', 'age', 'avatar', 'password')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'

class ProductForm(forms.ModelForm):
	is_new = forms.BooleanField(label='Новый товар')

	class Meta:
		model = Product
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'

