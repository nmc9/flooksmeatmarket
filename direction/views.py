from django.shortcuts import render
from owner.models import Owner
from django.shortcuts import render, get_object_or_404

def index(request):
    owner = get_object_or_404(Owner, key=0)
    address = owner.address
    return render(request, 'direction/map.html', {'address':address})