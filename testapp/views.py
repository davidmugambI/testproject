from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from testapp.forms import UserRegForm,LaptopForm
# from django.contrib.auth.forms import UserCreationForm
from testapp.models import Laptop
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def PrintHello(request):
    # return HttpResponse("Hello WORLD")
    return render(request,'testapp/testpage.html')


def register(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your account has been successfully created")
            return redirect('login')
    else:
        # form = UserCreationForm()
        form = UserRegForm()
    dict = {'form':form}
    return render(request, 'testapp/register.html', dict)

@login_required
def save_laptop(request):
    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Device add successfully")
            # return HttpResponse('Laptop item added')
            return redirect('testapp:retrieve')
    else:
        form = LaptopForm()
    return render(request, 'testapp/lap_form.html', {'form':form})

@login_required
def retrieve_data(request):
    data = Laptop.objects.all()
    return render(request, 'testapp/display.html', {'data':data})

@login_required
def save_with_html(request):
    """How to save data using an html form"""
    if request.method == 'POST':
        data = Laptop() # create model instance
        data.lap_type = request.POST.get('lap_type')
        data.price = request.POST.get('price')
        data.issues = request.POST.get('issues')
        data.status = request.POST.get('status')
        # data = Laptop(lap_type=request.POST.get('lap_type'),
        # price=request.POST.get('price'),issues=request.POST.get('issues'),
        # status=request.POST.get('status'))
        data.save()
        messages.success(request, "Device add successfully")
        return redirect('testapp:retrieve')
    else:
        return render(request, 'testapp/html_form.html')

@login_required
def update_data(request,id):
    data = get_object_or_404(Laptop, id=id)
    if request.method == 'POST':
        form = LaptopForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, "Item successfully updated")
            return redirect('testapp:retrieve')
    else:
        form = LaptopForm(instance=data)
    return render(request, 'testapp/lap_form.html', {'form':form})

@login_required
def delete_date(request, id):
    Laptop.objects.filter(id=id).delete()
    data = Laptop.objects.all()
    return render(request,'testapp/display.html',{'data':data})