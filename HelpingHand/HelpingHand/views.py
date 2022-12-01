from django.http import HttpResponse
from django.shortcuts import render, redirect
from Users.models import UserData
from Details.models import Details
from math import ceil
from django.contrib import messages


def index(request):
    return render(request,'index.html')

def signin(request):
    return render(request, 'signin.html')


def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        print(name,phone,email,password)

        ins = UserData(name=name,phone=phone,email=email,password=password)
        check = ins.save()
        print(check)
        messages.success(request, "Details Added Successfully.")
        return redirect('/signup')

    return render(request,'signup.html')

def options(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        password = request.GET.get('password')
        if UserData.objects.filter(email=email,password=password).exists():
            return render(request, 'options.html')
        else:
            return HttpResponse("Invalid Email or password")
    return HttpResponse("Error")

def details(request):
    if request.method == 'POST':
        image = request.POST['image']
        address = request.POST['address']
        description = request.POST['description']
        print(image,address,description)
        ins = Details(image=image,address=address,description=description)
        ins.save()
        messages.success(request, "Details Added Successfully.")
        return redirect('/details')

    return render(request, 'details.html')

def persons(request):
    persons = Details.objects.all()
    print(persons)
    n = len(persons)
    nSlides = n // 4 + ceil((n / 4) + (n // 4))
    params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'person': persons}
    return render(request, 'persons.html',params)

def filter(request):
    if request.method == 'GET':
        location = request.GET.get('location')
        filter_persons = Details.objects.filter(address=location).all()
        print(filter_persons)
        n = len(filter_persons)
        print(n)
        nSlides = n // 4 + ceil((n / 4) + (n // 4))
        print(nSlides)
        params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'person': filter_persons}
    return render(request,'filter_persons.html',params)



