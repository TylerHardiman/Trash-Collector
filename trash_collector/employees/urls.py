from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the user stories, add a path for each in urlpatterns

app_name = "employees"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.create, name="create"),
    path('edit_profile/', views.edit_employee_profile, name="edit_profile"),
    path('<int:customer_id>/pickup_confirmed', views.pickup_confirmed, name='pickup_confirmed'),
    path('all_customers/', views.all_customers, name="all_customers"),
    path('<str:day>/day_filter/', views.day_filter, name="day_filter")
]