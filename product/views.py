from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.cache import cache_control
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from home.models import Product, OrderLine


def index(request, basketAdded=0):
    all_product = Product.objects.all()
    context = {'all_product': all_product, 'searchby': 'XX'}

    if basketAdded:
        context['basketAdded'] = 'Item was added to basket'
    current_user = request.user
    basketAdded=0

    # display to user or display to customer
    if current_user.groups.filter(name='Employee').exists():
        return render(request, 'product/productEmployee.html', context)
    else:
        return render(request, 'product/productCustomer.html', context)


def productSearch(request, searchby, basketAdded=0):
    # Filter out by type choice
    user_filter = ''
    if request.method == 'POST':
        searchby = request.POST['_user_type']
        user_filter = request.POST['user_search']

    if searchby == 'AL':
        # Display all that fall under the meat category
        all_product = Product.objects.all().filter(
            Q(type='Beef') | Q(type='Poultry') | Q(type='Pork') |
            Q(type='Specialty Meats')).filter(name__icontains=user_filter)
    elif searchby == 'BF':
        all_product = Product.objects.all().filter(type='Beef').filter(name__icontains=user_filter)
    elif searchby == 'PK':
        all_product = Product.objects.all().filter(type='Pork').filter(name__icontains=user_filter)
    elif searchby == 'PT':
        all_product = Product.objects.all().filter(type='Poultry').filter(name__icontains=user_filter)
    elif searchby == 'SM':
        all_product = Product.objects.all().filter(type='Specialty Meats').filter(name__icontains=user_filter)
    elif searchby == 'DI':
        all_product = Product.objects.all().filter(type='Deli').filter(name__icontains=user_filter)
    elif searchby == 'GS':
        all_product = Product.objects.all().filter(type='Groceries').filter(name__icontains=user_filter)
    else:
        # Default catch just display all
        all_product = Product.objects.all().filter(name__icontains=user_filter)

    context = {'all_product': all_product, 'searchby': searchby}
    if basketAdded:
        context['basketAdded'] = 'Item was added to basket'

    current_user = request.user
    # display to user or display to customer
    if current_user.groups.filter(name='Employee').exists():
        return render(request, 'product/productEmployee.html', context)
    else:
        return render(request, 'product/productCustomer.html', context)

@login_required(login_url='/login/')
def productAddBasket(request, pk):
    current_user = request.user
    basket = current_user.basket
    product = get_object_or_404(Product,pk=pk)
    order = OrderLine(basket=basket, product=product, quantity=1)
    order.save()
    return redirect('product:index', basketAdded=1)


class ProductAdd(CreateView):
    model = Product
    fields = ['name', 'description', 'price', 'type',
              'location', 'byPound']

    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def dispatch(self, *args, **kwargs):
        current_user = self.request.user
        if current_user.groups.filter(name='Employee').exists():
            context = super(ProductAdd, self).dispatch(self.request, *args, **kwargs)
            return context
        else:
            return redirect('product:index')


class ProductUpdate(UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'type',
              'location', 'byPound']

    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def dispatch(self, *args, **kwargs):
        current_user = self.request.user
        if current_user.groups.filter(name='Employee').exists():
            context = super(ProductUpdate, self).dispatch(self.request, *args, **kwargs)
            return context
        else:
            return redirect('product:index')


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('product:index')

    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def dispatch(self, *args, **kwargs):
        current_user = self.request.user
        if current_user.groups.filter(name='Employee').exists():
            context = super(ProductDelete, self).dispatch(self.request, *args, **kwargs)
            return context
        else:
            return redirect('product:index')
