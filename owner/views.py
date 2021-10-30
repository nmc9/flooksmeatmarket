from django.contrib.auth.models import User, Group
from django.core.validators import validate_email
from django.views.decorators.cache import cache_control
from .models import Owner
from django.shortcuts import render, get_object_or_404, redirect
import re
from django import forms


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    if not request.user.groups.filter(
            name='Owner').exists():
        return redirect('home:home')
    template_name = 'owner/index.html'
    return render(request, template_name)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def companyInfo(request):
    if not request.user.groups.filter(
            name='Owner').exists():
        return redirect('home:home')
    template_name = 'owner/companyInfo-form.html'
    key_settings = 0
    info = get_object_or_404(Owner, key=key_settings)
    sundaySS = info.SundayStart.strftime("%H:%M")
    sundaySE = info.SundayEnd.strftime("%H:%M")
    saturdaySaS = info.SaturdayStart.strftime("%H:%M")
    saturdaySaE = info.SaturdayEnd.strftime("%H:%M")
    weekdayS = info.WeekdayStart.strftime("%H:%M")
    weekdayE = info.WeekdayEnd.strftime("%H:%M")
    # saturday = info.OpenSaturday
    # sunday = info.OpenSunday
    context = {'info': info, 'sundaySS': sundaySS, 'sundaySE': sundaySE, 'saturdaySaS': saturdaySaS,
               'saturdaySaE': saturdaySaE, 'weekdayS': weekdayS, 'weekdayE': weekdayE}

    return render(request, template_name, context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def updateCompanyInfo(request):
    if not request.user.groups.filter(
            name='Owner').exists():
        return redirect('home:home')

    if request.method == 'POST':
        template_name = 'owner/companyInfo-form.html'
        key_settings = 0
        info = get_object_or_404(Owner, key=key_settings)
        sundaySS = info.SundayStart.strftime("%H:%M")
        sundaySE = info.SundayEnd.strftime("%H:%M")
        saturdaySaS = info.SaturdayStart.strftime("%H:%M")
        saturdaySaE = info.SaturdayEnd.strftime("%H:%M")
        weekdayS = info.WeekdayStart.strftime("%H:%M")
        weekdayE = info.WeekdayEnd.strftime("%H:%M")
        # Error Checking Variables
        context = {'info': info, 'sundaySS': sundaySS, 'sundaySE': sundaySE, 'saturdaySaS': saturdaySaS,
                   'saturdaySaE': saturdaySaE, 'weekdayS': weekdayS, 'weekdayE': weekdayE}
        error_found = False  # flag to send error message

        SS = request.POST['id_SundayStart']
        SE = request.POST['id_SundayEnd']
        SaS = request.POST['id_SaturdayStart']
        SaE = request.POST['id_SaturdayEnd']
        weekS = request.POST['id_WeekdayStart']
        weekE = request.POST['id_WeekdayEnd']

        '''
        The phone number regex is code from
        http://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
        '''
        # if the time fits the time format then it can be used.
        # otherwise it will trigger an error route
        if re.compile("^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$").match(SS):
            info.SundayStart = SS
        else:
            error_found = True
            context['error_SS'] = 'Invalid Start Time'

        if re.compile("^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$").match(SE):
            info.SundayEnd = SE
        else:
            error_found = True
            context['error_SE'] = 'Invalid End Time'

        if re.compile("^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$").match(SaS):
            info.SaturdayStart = SaS
        else:
            error_found = True
            context['error_SaS'] = 'Invalid Start Time'

        if re.compile("^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$").match(SaE):
            info.SaturdayEnd = SaE
        else:
            error_found = True
            context['error_SaE'] = 'Invalid End Time'

        if re.compile("^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$").match(weekS):
            info.WeekdayStart = weekS
        else:
            error_found = True
            context['error_weekS'] = 'Invalid Start Time'

        if re.compile("^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$").match(weekE):
            info.WeekdayEnd = weekE
        else:
            error_found = True
            context['error_weekE'] = 'Invalid End Time'


        # if the phone number doesn't match the regex then start error
        if re.compile("^\+?1?\d{9,15}$").match(request.POST['id_phone_number']):
            info.phone_number = request.POST['id_phone_number']
        else:
            error_found = True
            error_phone = "Phone number must be entered in the format: '+999999999'. Between 9 and 15 digits allowed."
            context['error_phone'] = error_phone

        # Set the fields to string variables to check them


        Vname = request.POST['id_name']
        if not validation(Vname):
            print(1)
            context['error_Vname'] = 'Invalid Character Input'
            error_found = True
        Vaddress = request.POST['id_address']
        if not validation(Vaddress):
            context['error_Vaddress'] = 'Invalid Character Input'
            error_found = True

        VOpenFromWD = request.POST['id_OpenFromWD']
        if not validation(VOpenFromWD):
            context['error_VOpenFromWD'] = 'Invalid Character Input'
            error_found = True
        VOpenUntilWD = request.POST['id_OpenUntilWD']
        if not validation(VOpenUntilWD):
            context['error_VOpenUntilWD'] = 'Invalid Character Input'
            error_found = True

        VNotes = request.POST['id_Notes']
        if not validation(VNotes):
            context['error_Vnotes'] = 'Invalid Character Input'
            error_found = True
        Vemail = request.POST['id_email']
        try:
            validate_email(Vemail)

        except forms.ValidationError:
            context['error_VEmail'] = 'Please Enter A Valid Email'
            error_found = True

        # If a problem was found redirect back to form
        if error_found:
            return render(request, template_name, context)
        info.email = Vemail
        info.Notes = VNotes
        info.OpenUntilWD = VOpenUntilWD
        info.OpenFromWD = VOpenFromWD
        info.name = Vname
        info.address = Vaddress

        if 'id_OpenSunday' in request.POST:
            info.OpenSunday = True
        else:
            info.OpenSunday = False
        if 'id_OpenSaturday' in request.POST:
            info.OpenSaturday = True
        else:
            info.OpenSaturday = False

        info.save()

        return redirect('owner:index')
    else:
        return redirect('owner:CompanyInfo')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def updateUser(request):
    if not request.user.groups.filter(
            name='Owner').exists():
        return redirect('home:home')

    template_name = 'owner/update_user.html'
    # Remove the Owner from the list of users
    owner = User.objects.all().filter(groups__name='Owner').exclude(username='admin')  # Don't show developer Account
    customer = User.objects.all().filter(groups__name='Customer').exclude(groups__name='Employee').exclude(
        is_active=False)
    employee = User.objects.all().filter(groups__name='Employee').exclude(groups__name='Owner').exclude(is_active=False)
    inactive = User.objects.all().filter(is_active=False)
    context = {'all_customer': customer, 'all_employee': employee, 'all_owner': owner, 'all_inactive': inactive}
    return render(request, template_name, context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def makeEmployee(request, user_id):
    makeEmp = get_object_or_404(User, pk=user_id)
    empGroup = Group.objects.get(name='Employee')
    empGroup.user_set.add(makeEmp)

    return redirect('owner:update-user')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def removeEmployee(request, user_id):
    removeEmp = get_object_or_404(User, pk=user_id)
    empGroup = Group.objects.get(name='Employee')
    empGroup.user_set.remove(removeEmp)

    return redirect('owner:update-user')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def deactivateUser(request, user_id):
    deAct = get_object_or_404(User, pk=user_id)
    deAct.is_active = False
    deAct.save()
    return redirect('owner:update-user')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def reactivateUser(request, user_id):
    reAct = get_object_or_404(User, pk=user_id)
    reAct.is_active = True
    reAct.save()
    return redirect('owner:update-user')


def validation(validation_string):
    validation_string = validation_string.replace(" ", "")
    ''' The validation pattern with a few changes is from
        http://stackoverflow.com/questions/29460405/checking-if-string-is-only-letters-and-spaces-python
        '''
    if re.match("^[A-Za-z0-9_-]*$", validation_string):
        print(validation_string)
        return True
    return False
