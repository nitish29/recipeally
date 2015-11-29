from django import forms
from recipesearch.models import Comments

from recipesearch.models import User
from recipesearch.models import UserProfile
class SignUpForm(forms.ModelForm):
	class Meta:
		model=User
		fields=['username','first_name','last_name','email','password']
		widgets = {
            'password': forms.PasswordInput(),
        }

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
		for fieldname in ['username']:
			self.fields[fieldname].help_text = None
	def clean_email(self):
		email=self.cleaned_data.get('email')
		email_base,provider=email.split("@")
		domain,extension=provider.split('.')
		if not extension == "edu":
			raise forms.ValidationError("Use edu address")
		return email

class ProfileForm(forms.ModelForm):
	class Meta:
		model=UserProfile
		fields=['user_about']

# class PostForm(forms.ModelForm):
# 	class Meta:
# 		model=Comments
#     	fields=['comment_text']


class PostForm(forms.ModelForm):
	class Meta:
		model=Comments
		fields=['comment_text']