from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from django import forms

# from .models import InternshipPost, OpenSourcePost

class UserCreateForm(UserCreationForm):
	class Meta:
       
		fields = ('email','username','password1', 'password2')
		model = get_user_model()
      
		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			self.fields['username'].label.widget.attrs.update({'class': 'form-control'})
			self.fields['email'].label.widget.attrs.update({'class': 'form-control'})

# class HospitalDataCreateForm(forms.ModelForm):
# 	class Meta:
# 		model = InternshipPost
# 		fields = [
# 			'title',
# 			'description',
# 			'last_date',
# 			'registration_link',
# 			'recruiter_name',
# 			'recruiter_phone',
# 			'recruiter_email',
# 		]


