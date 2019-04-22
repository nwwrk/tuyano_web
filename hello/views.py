from django.shortcuts import render,redirect
from django.db.models import Q
from .models import Person

def index(request, num=1000):
    if request.method == 'POST':
        name_str = request.POST['name']
        mail_str = request.POST['mail']
        age_int = request.POST['age']
        obj = Person(name=name_str, mail=mail_str, age=age_int)
        obj.save()
    else:
        obj = Person()

    data = Person.objects.all()
    name_str = ''

    context = {
        'title': 'hello/index',
        'msg': 'Person\'s List',
        'current': obj,
        'data': data,
    }

    return render(request, 'hello/index.html', context)

def update(request, id):
    current = Person.objects.get(id=id)
    if request.method == 'POST':
        current.name = request.POST['name']
        current.mail = request.POST['mail']
        current.age = request.POST['age']
        current.save()
        return redirect('index')

    context = {
        'title': 'hello/update',
        'msg': 'Person ID='+str(id)+' update.',
        'current': current,
    }
    return render(request, 'hello/update.html', context)

def delete(request, id):
    current = Person.objects.get(id=id)
    current.delete()
    return redirect('index')
