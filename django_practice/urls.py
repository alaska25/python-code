from django.urls import path

from . import views

app_name = 'grocerylist'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:groceryitem_id>/', views.groceryitem, name='viewgroceryitem'),
	# /grocerylist/register
	path('register', views.register, name="register"),
	# /grocerylist/change_password
	path('change_password', views.change_password, name='change_password'),
	# /grocerylist/login
	path('login', views.login_view, name='login'),
	# /grocerylist/logout
	path('logout', views.logout_view, name="logout"),
	# /grocerylist/add_item
	path('add_item', views.add_item, name='add_item'),
	# /grocerylist/<groceryitem_id>/edit
	path('<int:groceryitem_id>/edit', views.update_item, name='update_item'),
	# /grocerylist/<groceryitem_id>/delete
	path('<int:groceryitem_id>/delete', views.delete_item, name='delete_item'),
]

