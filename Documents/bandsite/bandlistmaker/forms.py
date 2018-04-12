from django import forms
from .models import *
from django.forms import ModelChoiceField

class MyModelChoiceField(ModelChoiceField):
	def label_from_instance(self, obj):
		return "%s" % obj.year + " %s" % obj.name
		
class MembersForm(forms.Form):

	id = forms.CharField(label='ID',max_length=6,required=True)
	name = forms.CharField(label='名前',max_length=20,required=True)
	email = forms.EmailField(label='Email',required=False)
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['id'].widget.attrs['class'] = 'form-control'
		self.fields['name'].widget.attrs['class'] = 'form-control'
		self.fields['email'].widget.attrs['class'] = 'form-control'
		
class BandsForm(forms.Form):
	name = forms.CharField(label='名前',max_length=20,required=True)
	video_url = forms.URLField(label='URL',required=False)
	seasons = MyModelChoiceField(label='Season',queryset=Seasons.objects.all(),required=True)
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['name'].widget.attrs['class'] = 'form-control'
		self.fields['video_url'].widget.attrs['class'] = 'form-control'
		
class SeasonsForm(forms.Form):
	name = forms.CharField(label='名前',max_length=20,required=True)
	year = forms.CharField(label='年',max_length=4,required=True)
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['name'].widget.attrs['class'] = 'form-control'
		self.fields['year'].widget.attrs['class'] = 'form-control'

class EditMembersForm(forms.Form):
	name = forms.CharField(label='名前',max_length=20,required=True)	
	email = forms.EmailField(label='Email',required=False)
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['name'].widget.attrs['class'] = 'form-control'
		self.fields['email'].widget.attrs['class'] = 'form-control'

class AddBandMemberForm(forms.Form):
	members = forms.ModelMultipleChoiceField(label='Members',queryset=Members.objects.all(),widget=forms.CheckboxSelectMultiple, required=False)
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
