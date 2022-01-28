from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from datetime import date

from trash_collector import customers
from .models import Employee
from django.apps import apps

from .filters import DayFilter

# from .models import User


# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.

@login_required
def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db for Customers
    Customer = apps.get_model('customers.Customer') # Customer database is being loaded into the variable
    # Filtering from customer variable the day of the week for pickup
    #
    today = date.today() # 2022-01-26
    day_names =['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    todays_weekday_index = today.weekday() # 3
    name_of_today = day_names[todays_weekday_index] # 'Wednesday'

    logged_in_employee = request.user
    

    try:

        logged_in_employee = Employee.objects.get(user=logged_in_employee)

        customers_zipcode = Customer.objects.filter(zip_code=logged_in_employee.zip_code)
        customer_pickups_today = customers_zipcode.filter(weekly_pickup=name_of_today) | customers_zipcode.filter(one_time_pickup=today)
        non_suspended_accounts = customer_pickups_today.exclude(suspend_start__lt=today, suspend_end__gt=today)
        final_customers_pickup = non_suspended_accounts.exclude(date_of_last_pickup=today)
        
        context = {
            'logged_in_employee': logged_in_employee,
            'customers': final_customers_pickup ,
            'today': today
        }
        return render(request, 'employees/index.html', context)
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('employees:create'))



def filter_day(request, all_customers):
    myFilter = DayFilter(request.GET, queryset=all_customers)
    all_customers = customers
    context = {
            'myFilter':myFilter
        }
    return render(request, 'employees/index.html', context)


# def filter_day(request):
#     Customer = apps.get_model('customers.Customer') # 


#     # today = date.today() # 2022-01-26
#     day_names =['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] 
    
#     myFilter = DayFilter(request.GET, queryset=all_customers)
#     customers = myFilter.qs

#     context = {
#             'day_names': day_names,
#             'myFilter':myFilter
#         }
      
#     return render(request, 'employees/index.html', context)


@login_required
def create(request):
    logged_in_user = request.user
    if request.method == "POST":
        name_from_form = request.POST.get('name')
        address_from_form = request.POST.get('address')
        zip_from_form = request.POST.get('zip_code')
        logged_in_employee = Employee(name=name_from_form, user=logged_in_user, address=address_from_form, zip_code=zip_from_form)
        logged_in_employee.save()

        return HttpResponseRedirect(reverse('employees:index' ))
    else:
        return render(request, 'employees/create.html')

@login_required
def edit_employee_profile(request):
    logged_in_user = request.user
    logged_in_employee = Employee.objects.get(user=logged_in_user)
    if request.method == "POST":
        name_from_form = request.POST.get('name')
        address_from_form = request.POST.get('address')
        zip_from_form = request.POST.get('zip_code')
        logged_in_employee.name = name_from_form
        logged_in_employee.address = address_from_form
        logged_in_employee.zip_code = zip_from_form
        logged_in_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        context = {
            'logged_in_employees': logged_in_employee
        }
        return render(request, 'employees/edit_profile.html', context)


@login_required
def pickup_confirmed(request, customer_id):
    Customer = apps.get_model('customers.Customer')
    update_last_pickup = Customer.objects.get(id=customer_id)
    update_last_pickup.date_of_last_pickup = date.today()
    update_last_pickup.save()
    charge_customer(request, customer_id)

    return HttpResponseRedirect(reverse('employees:index'))
    # return render(request, 'employees/index.html')


@login_required
def charge_customer(request, customer_id):
    Customer = apps.get_model('customers.Customer')
    update_current_balance = Customer.objects.get(id=customer_id)
    update_current_balance.balance += 20
    update_current_balance.save()
    
    

@login_required
def all_customers(request, customer_id):
    # This line will get the Customer model from the other app, it can now be used to query the db for Customers
    Customer = apps.get_model('customers.Customer') # Customer database is being loaded into the variable

    all_customers = Customer.objects.all(customer_id)
    
    context = {
          
            'all_customers': all_customers
           
        }
        
    return render(request, 'employees/all_customers.html', context)

    # try:
        
    #     
    # except ObjectDoesNotExist:
        # return HttpResponseRedirect(reverse('employees:index'))
