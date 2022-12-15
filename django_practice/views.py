from django.shortcuts import render, redirect, get_object_or_404
from .models import GroceryItem
from .forms import LoginForm, AddItemForm, UpdateItemForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict
from django.utils import timezone

# Create your views here.
def index(request):
	groceryitem_list = GroceryItem.objects.filter(user_id=request.user.id)
	context = {
		'groceryitem_list': groceryitem_list,
		'user': request.user
	}
	return render(request, "grocerylist/index.html", context)

def groceryitem(request, groceryitem_id):
	groceryitem = get_object_or_404(GroceryItem, pk=groceryitem_id)
	return render(request, "grocerylist/groceryitem.html", model_to_dict(groceryitem))

def register(request):
	users = User.objects.all()
	is_user_registered = False
	context = {
		"is_user_registered": is_user_registered
	}

	for indiv_user in users:
		if indiv_user.username == "johndoe":
			is_user_registered = True
			break


	if is_user_registered == False:
		user = User()
		user.username = "janedoe"
		user.first_name = "Jane"
		user.last_name = "Doe"
		user.email = "jane@mail.com"
		user.set_password("jane1234")
		user.is_staff = False
		user.is_active = True
		user.save()
		context ={
			"first_name": user.first_name,
			"last_name": user.last_name
		}

	return render(request, "grocerylist/register.html", context)

def change_password(request):

	is_user_authenticated = False

	user = authenticate(username="johndoe", password="john1234")
	print(user)
	if user is not None:
		authenticated_user = User.objects.get(username='johndoe')
		authenticated_user.set_password("johndoe1")
		authenticated_user.save()
		is_user_authenticated = True
		context = {
			"is_user_authenticated": is_user_authenticated
		}

		return render(request, "grocerylist/change_password.html", context)

def login_view(request):
	context = {}

	if request.method == 'POST':
		form = LoginForm(request.POST)

		if form.is_valid() == False:
			form = LoginForm()

		else:
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			context = {
				"username": username,
				"password": password
			}

			if user is not None:
				login(request, user)
				return redirect("grocerylist:index")
			else:
				context = {
					"error": True
				}

	return render(request, "grocerylist/login.html", context)

def logout_view(request):
	logout(request)
	return redirect("grocerylist:index")

def add_item(request):
	context = {
       "user": request.user
    }

	if request.method == 'POST':
		form = AddItemForm(request.POST)

		if form.is_valid() == False:
			form = AddItemForm()
		else:
			item_name = form.cleaned_data['item_name']
			category = form.cleaned_data['category']

			duplicates = GroceryItem.objects.filter(item_name=item_name)

			if not duplicates:
				GroceryItem.objects.create(item_name=item_name, category=category, date_created=timezone.now(), user_id=request.user.id)
				return redirect('grocerylist:index')

			else:
				context = {
					"error": True
				}

	return render(request, "grocerylist/add_item.html", context)


def update_item(request, groceryitem_id):

	groceryitem = GroceryItem.objects.filter(pk=groceryitem_id)

	context = {
		"user": request.user,
		"groceryitem_id": groceryitem_id,
		"item_name": groceryitem[0].item_name,
		"category": groceryitem[0].category,
		"status": groceryitem[0].status
	}

	if request.method == 'POST':
		form = UpdateItemForm(request.POST)

		if form.is_valid() == False:
			form = UpdateItemForm()
		else:
			item_name = form.cleaned_data['item_name']
			category = form.cleaned_data['category']
			status = form.cleaned_data['status']

			if groceryitem:
				groceryitem[0].item_name = item_name
				groceryitem[0].category = category
				groceryitem[0].status = status

				groceryitem[0].save()
				return redirect("grocerylist:index")
			else:
				context = {
					"error": True
				}

	return render(request, "grocerylist/update_item.html", context)

def delete_item(request, groceryitem_id):
	groceryitem = GroceryItem.objects.filter(pk=groceryitem_id).delete()
	return redirect("grocerylist:index")
