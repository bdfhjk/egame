from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.templatetags.static import static
from core.models import Building, BuildingState
from django.forms.models import model_to_dict
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):

    if 'logout' in request.GET:
        logout(request)
        return index(request)
    template = loader.get_template('core/index.html')
    return HttpResponse(template.render())

def buildings(request):
    template = loader.get_template('core/buildings.html')

    buildings_raw = Building.objects.all().order_by('number')
    buildings_processed = []
    for building in buildings_raw:
        level = BuildingState.objects.get(building__name=building.name).level
        raw = model_to_dict(building)
        raw['level'] = level
        raw['icon'] = static(raw['icon'])
        if raw['level'] != 'Unavailable':
            buildings_processed.append(raw)

    building_rows = []
    count = 0
    row = []
    for building in buildings_processed:
        count = count + 1
        row.append(building)
        if count == 3:
            count = 0
            building_rows.append(row)
            row = []

    if (row != []):
        building_rows.append(row)

    context = RequestContext(request, {
        'building_rows': building_rows,
    })
    return HttpResponse(template.render(context))

def citizens(request):
    template = loader.get_template('core/citizens.html')
    return HttpResponse(template.render())

def login(request):
    context = RequestContext(request, {})
    template = loader.get_template('core/login.html')

    if 'username' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return index(request)
        else:
            return HttpResponse(template.render(context))
    else: 
        return HttpResponse(template.render(context))
