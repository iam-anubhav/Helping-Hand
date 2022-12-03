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

        details = [name,phone,email,password]
        if '' in details:
            messages.success(request, "Some field is empty")
            return redirect('/signup')
        elif len(phone) < 10 or len(phone) > 10:
            messages.success(request, "Invalid phone")
            return redirect('/signup')
        elif '@' not in email:
            messages.success(request, "Invalid Email")
            return redirect('/signup')
        else:
            ins = UserData(name=name, phone=phone, email=email, password=password)
            ins.save()
            messages.success(request, "Details Added Successfully. Sign in now")
            return redirect('/signup')

    return render(request,'signup.html')

def options(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        password = request.GET.get('password')
        if (email=='') or (password==''):
            messages.success(request,"One of the field is empty")
            return redirect('/signin')
        elif UserData.objects.filter(email=email,password=password).exists() == False:
            messages.success(request, "Invalid Email or Password")
            return redirect('/signin')
        else:
            return render(request, 'options.html')
    return render(request,'options.html')

def details(request):
    if request.method == 'POST':
        image = request.POST['image']
        address = request.POST['address']
        description = request.POST['description']
        if address=='' and description=='':
            messages.success(request,"Enter Address and description")
        elif address == '':
            messages.success(request,"Enter Address")
        elif description == '':
            messages.success(request,"Enter Description")
        else:
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
    params = {'all_persons':n, 'no_of_slides': nSlides, 'range': range(1, nSlides), 'person': persons}
    return render(request, 'persons.html',params)

def filter(request):
    if request.method == 'GET':
        location = request.GET.get('location')
        filter_persons = Details.objects.filter(address=location).all()
        n = len(filter_persons)
        nSlides = n // 4 + ceil((n / 4) + (n // 4))
        params = {'all_persons': n, 'no_of_slides': nSlides, 'range': range(1, nSlides), 'person': filter_persons}
    return render(request,'filter_persons.html',params)



