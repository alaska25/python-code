from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(label='Username', max_length=20)
	password = forms.CharField(label='Password', max_length=20)

class AddItemForm(forms.Form):
	item_name = forms.CharField(label='Item Name', max_length=50)
	category = forms.CharField(label='Category', max_length=200)

class UpdateItemForm(forms.Form):
	item_name = forms.CharField(label='Item Name', max_length=50)
	category = forms.CharField(label='Category', max_length=200)
	status = forms.CharField(label='Status', max_length=50)
