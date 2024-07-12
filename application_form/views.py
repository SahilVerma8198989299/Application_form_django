from django.http import HttpResponse
from django.shortcuts import render
from form_en.models import form_enquirys


def form(request):
    if request.method == 'POST':
        first=request.POST.get('first')
        last=request.POST.get('last')

        email=request.POST.get('email')

        job=request.POST.get('job')
        address=request.POST.get('address')

        city=request.POST.get('cityy')

        pincode=request.POST.get('pin')
        # dat=request.POST.get('datee')
    # full_name=first + " " + last
        full_name = "{} {}".format(first, last)
        print(full_name)

   
    
        enquiry=form_enquirys(full_name=full_name,email=email, job_role=job, address=address, city=city, pincode=pincode)
        enquiry.save()

   
    return render(request, "job application form.html")



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