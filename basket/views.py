from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.cache import cache_control

from home.models import OrderLine


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/login/')
def index(request):
    template_name = 'basket/userlist.html'
    all_user = User.objects.all()
    context = {'all_user': all_user}
    current_user = request.user
    if current_user.groups.filter(name='Owner').exists() or current_user.groups.filter(name='Employee').exists():
        return render(request, template_name, context)
    return redirect('basket:detail', current_user.id)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/login/')
def basketDetail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    current_user = request.user
    context = user.first_name

    # If correct user OR an Employee access this basket
    # check userId with the id of the basket
    if user == current_user:
        return render(request, 'basket/basketDetail.html', {'user': user, 'context': context, 'column': 'Amount', 'save':True})
    if current_user.groups.filter(name='Employee').exists():
        # save button on basket hidden?
        save = False
        if current_user.groups.filter(name='Owner').exists():
            # only Owner can edit another users basket
            save = True
        return render(request, 'basket/basketDetail.html', {'user': user, 'context': context, 'column': 'Amount', 'save':save})
    return redirect('basket:detail', current_user.id)  # redirects to their basket


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/login/')
def basketDetail_column(request, user_id, column):
    user = get_object_or_404(User, pk=user_id)
    current_user = request.user
    context = user.first_name
    # If correct user OR an Employee access this basket
    # check userId with the id of the basket
    if user == current_user:
        return render(request, 'basket/basketDetail.html',
                      {'user': user, 'context': context, 'column': column, 'save': True})
    if current_user.groups.filter(name='Employee').exists():
        # save button on basket hidden?
        save = False
        if current_user.groups.filter(name='Owner').exists():
            # only Owner can edit another users basket
            save = True
        return render(request, 'basket/basketDetail.html',
                      {'user': user, 'context': context, 'column':column, 'save': save})
    return redirect('basket:detail', current_user.id)  # redirects to their basket


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/login/')
def edit(request, user_id):

    user = get_object_or_404(User, pk=user_id)
    current_user = request.user
    if request.method == 'POST':
        # If correct user OR Owner access this basket
        if user == current_user or current_user.groups.filter(name='Owner').exists():
            context = user.first_name
            save=True
            orders = user.basket.orderline_set.all()

            for i in orders:

                strin = str(i.pk) + "quantity"
                # Error Check: if value is a float continue
                try:
                    value = float(request.POST[strin])
                except:
                    error = 'Please Enter a Number'
                    return render(request, 'basket/basketDetail.html',
                                  {'user': user, 'context': context, 'error': error, 'column':'Amount','save':save})

                if i.product.byPound and (i.quantity * 10) % 5 == 0.0:
                    pass
                elif (not i.product.byPound) and i.quantity % 1 == 0.0:
                    pass
                else:
                    error = 'Invalid Input'
                    return render(request, 'basket/basketDetail.html',
                                  {'user': user, 'context': context, 'error': error, 'column':'Amount','save':save})
                i.quantity = value
                i.save()
                if i.quantity == 0:
                    instance = OrderLine.objects.get(id=i.id)
                    print(instance)
                    instance.delete()
            rawdate = request.POST['id_Dateinput']
            if not rawdate == "":
                try:
                    formattedDate = datetime.strptime(rawdate, '%m/%d/%y')
                except ValueError:
                    error_date = 'Invalid Date Format'
                    return render(request, 'basket/basketDetail.html',
                                {'user': user, 'context': context, 'error_date': error_date, 'column':'Amount','save':save})

                user.basket.Date = formattedDate
            else:
                user.basket.Date = None
            user.basket.save()

            return render(request, 'basket/basketDetail.html', {'user': user, 'context': context, 'column':'Amount','save':save})
        return redirect('basket:detail', current_user.id)
    else:
        return redirect('basket:detail', current_user.id)

