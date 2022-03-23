from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
	title = forms.CharField()
	business_name = forms.CharField()
	email = forms.EmailField()

	class Meta(UserCreationForm.Meta):
		model = User
		fields = UserCreationForm.Meta.fields + ("email","title","business_name")
