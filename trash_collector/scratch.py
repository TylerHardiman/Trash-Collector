

# #---FOR Updating pickup date 

# def update(request, hero_id):
#   update_hero = Superhero.objects.get(pk=hero_id)
#   context = {
#       'hero' : update_hero
#   }

#   if request.method == "POST":
#     update_hero.name = request.POST.get('name')
#     update_hero.alter_ego = request.POST.get('alter_ego')
#     update_hero.primary_ability = request.POST.get('primary')        
#     update_hero.secondary_ability = request.POST.get('secondary')
#     update_hero.catch_phrase = request.POST.get('catchphrase')
    
#     # update_hero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary, secondary_ability=secondary, catch_phrase=catchphrase)
#     update_hero.save()
    
#     return HttpResponseRedirect(reverse('superheroes:index'))

#   else:
#     return render(request, 'superheroes/update.html', context)
    


# def delete_hero(request, hero_id):
#   single_hero = Superhero.objects.get(pk=hero_id)
#   # context = {
#   #   'hero': single_hero
#   # }
#   # if request.method == 'POST':
#   single_hero.delete()

#   return HttpResponseRedirect(reverse('superheroes:index'))


# path('<int:hero_id>/delete', views.delete_hero, name='delete')

# <a href="{% url 'superheroes:delete' hero.id %}">Delete this Hero</a><br />


# @login_required # possibly add balance?
# def calculate_balance(request, sum, balance, customer_id):
#     Customer = apps.get_model('customers.Customer')
#     current_balance = Customer.objects.get(id=customer_id)
#     a = int(20)
#     b = balance
#     current_balance = a + b
#     print('sum:', sum)