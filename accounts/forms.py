from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		fields = UserCreationForm.Meta.fields + ("email",)