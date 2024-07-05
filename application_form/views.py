from django.http import HttpResponse
from django.shortcuts import render

def form(request):
    first=request.POST.get('first')
    last=request.POST.get('last')

    email=request.POST.get('email')

    job=request.POST.get('job')
    address=request.POST.get('address')

    city=request.POST.get('cityy')

    pincode=request.POST.get('pin')
    datee=request.POST.get('datee')
    # full_name=first + last
    data={
        # 'full':full_name,
        'email_p':email,
        'job_role':job,
        'add':address,
        'ci':city,
        'pinn': pincode,
        'da':datee,
    }
    return render(request, "job application form.html", data)
def result(request):
    first=request.POST.get('first')
    last=request.POST.get('last')

    email=request.POST.get('email')

    job=request.POST.get('job')
    address=request.POST.get('address')

    city=request.POST.get('cityy')

    pincode=request.POST.get('pin')
    datee=request.POST.get('datee')
    full_name=first + " " + last
    data={
        'full':full_name,
        'email_p':email,
        'job_role':job,
        'add':address,
        'ci':city,
        'pinn': pincode,
        'da':datee,
    }
    return render(request, "resutt.html", data)