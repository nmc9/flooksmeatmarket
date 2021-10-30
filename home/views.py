from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.cache import cache_control
from django.views.generic import View
from owner.models import Owner

from .forms import UserForm, LoginForm
from .models import Group, Basket


def index(request):
    owner = get_object_or_404(Owner, key=0)
    pn = owner.phone_number
    phone_num = '(' + pn[:3] + ')-' + pn[3:-4] + '-' + pn[6:]

    return render(request, 'home/index.html', {'owner': owner, 'phone_num': phone_num})


class LoginView(View):
    form_class = LoginForm
    template_name = 'home/login.html'

    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def get(self, request):
        error_basket = ''
        if request.GET.get('next'):
            error_basket = 'You need to login to create a basket'
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form, 'error_basket': error_basket})

    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def post(self, request):
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home:home')
            else:
                error = 'Inactive login Credentials'
                return render(request, self.template_name, {'form': form, 'error': error})
        error = 'Invalid login Credentials'
        return render(request, self.template_name, {'form': form, 'error': error})


class UserFormView(View):
    form_class = UserForm
    template_name = 'home/registration.html'

    # blank form
    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            signup = form.cleaned_data['signup']
            email = form.cleaned_data['email']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    customergroup = Group.objects.get(name='Customer')
                    customergroup.user_set.add(user)
                    basket = Basket(User=user)
                    basket.save()
                    login(request, user)
                    return redirect('home:home')
        return render(request, self.template_name, {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home:login')


def FAQ(request):
    return render(request, 'home/FAQ.html')
