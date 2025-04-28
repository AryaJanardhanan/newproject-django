from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.

def home(request):
    return render(request, "home.html")

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def base(request):
    return render(request, "base.html")

def contact(request):
    if request.method == 'POST':
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        return render(request, "home.html")
    else:
        form = ContactForm()
    return render(request,"contact.html", {'form':form})

def students(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:   
        form = StudentForm()
    return render(request,"student.html", {'form':form})


def newstu(request):
    if request.method == 'POST':
        nam = request.POST.get('nm')
        ag = request.POST.get('ag')
        crs = request.POST.get('cr')
        st = Student(name=nam, age=ag, course=crs)
        st.save()
        return redirect('home')
    else:
        return render(request, "new_students.html")
    
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    else:
        form = RegisterForm()
    return render(request, "register.html", {'form':form})

def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            usrnm = form.cleaned_data['username']
            pswrd = form.cleaned_data['password']
            usr = authenticate(username=usrnm, password=pswrd)
            if usr is not None:
                login(request,usr)
                return redirect('home') 
            else:
                return "invalid username or password"
    else:
        form = SigninForm()
    return render(request,"signin.html", {'form':form})

def uslogout(request):
    logout(request)
    return redirect('signin')

def stlist(request):
    st = Student.objects.all()
    return render(request, "list.html", {'item':st})

def delt(request, pk):
    it = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        it.delete()
        return redirect('list')
    
def editt(request, pk):
    itm = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=itm)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = StudentForm(instance=itm)
    return render(request, "edit.html", {'form':form})

#CRUD
