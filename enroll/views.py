from django.http.response import HttpResponseRedirect
from django.shortcuts import render, HttpResponsePermanentRedirect
from .forms import StudentRegisteration
from .models import User

# Create your views here.

#This function adds new items and displays them.
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegisteration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            reg = User(name = name, email = email, password = password)
            reg.save()
            fm = StudentRegisteration()
    else:
        fm = StudentRegisteration()

    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud })

#This function will update or edit

def update_data(request, id):
    pi = User.objects.get(pk=id)
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = StudentRegisteration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect("/")
    else:
        fm = StudentRegisteration(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form': fm})


#This function will delete items.

def delete_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/")
        


