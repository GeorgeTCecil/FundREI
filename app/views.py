from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt
from .forms import *

# Create your views here.
def index(request):
    return render(request, "index.html")

def registration(request):
    errors = User.objects.user_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(first_name=request.POST["fname"], last_name=request.POST["lname"], email=request.POST["email"], password=pw_hash)
        request.session["userid"] = new_user.id
        return redirect("/home")

def login(request):
    try:
        User.objects.get(email=request.POST["email"])
    except:
        messages.error(request,"User does not exist.")
        return redirect("/")
    user = User.objects.get(email=request.POST['email']) 
    if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
        request.session["userid"] = user.id
        messages.success(request, "Successfully logged in!")
        return redirect("/home")
    else:
        messages.error(request, "Incorrect password.")
        return redirect("/")

def home(request):
    user = User.objects.get(id=request.session['userid'])
    context = {
        'projects': Project.objects.all(),
        'user': user
    }
    return render(request, "home.html", context)

def image_upload_view(request):
    """Process images uploaded by users"""
    user = User.objects.get(id=request.session['userid'])
    form_class = ProjectForm
    context = {
        'user': user
    }
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'add.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ProjectForm()
    return render(request, 'add.html', {'form': form})


def success(request): 
    return HttpResponse('successfully uploaded') 

def destroy(request, id):
    c = Project.objects.get(id=id)
    c.delete()
    return redirect('/home')

def add_project(request):
    user = User.objects.get(id=request.session['userid'])
    # user_projects = project.objects.filter(user=user)
    context = {
        'user': user
    }
    return render(request, 'add.html', context)

def new_project(request):
    # creator = request.user
    print(User.objects.get(id=request.session['userid']))
    errors = Project.objects.project_validator(request.POST)
    # form = ProjectForm(request.POST or None)
    
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    else:
        
        project = Project.objects.create(title=request.POST["title"], description=request.POST["description"], location=request.POST["location"], price=request.POST['price'], roi=request.POST['roi'], units=request.POST['units'], creator=User.objects.get(id=request.session['userid']))
        project.image = request.FILES['image']
        project.save()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
    
    # if form.is_valid():
    #     contact = form.save(commit=False)
    #     contact.owner = request.user
    #     contact.save()
    return redirect("/home")

def this_project(request, id):
    user = User.objects.get(id=request.session['userid'])
    context = {
        'project': Project.objects.get(id=id),
        'user': user,
    }
    return render(request, 'view.html', context)

def edit_project(request, id):
    user = User.objects.get(id=request.session['userid'])
    context = {
        'project': Project.objects.get(id=id),
        'user': user
    }
    return render(request, 'edit.html', context)

def update(request, id):
    project = Project.objects.get(id=id)
    project.title = request.POST['title']
    project.location = request.POST['location']
    project.description = request.POST['description']
    project.save()
    return redirect("/home")

def add_inv(request, user_id, project_id):
    my_user = User.objects.get(id=user_id)
    my_investment = Project.objects.get(id=project_id)
    my_user.invested_projects.add(my_investment)
    return redirect('/home')

def portfolio(request, user_id):
    user = User.objects.get(id=request.session['userid'])
    # my_investment = Project.objects.get(id=request.session['projectid'])
    # user.invested_projects.add(my_investment)
    context = {
        'user': user
    }
    return render(request, "portfolio.html", context)

def my_inv(request, user_id):
    user = User.objects.get(id=request.session['userid'])
    # my_investment = Project.objects.get(id=request.session['projectid'])
    # user.invested_projects.add(my_investment)
    context = {
        'user': user
    }
    return render(request, "myinv.html", context)

def update(request, id):
    project = Project.objects.get(id=id)
    # job.title = request.POST['title']
    # job.location = request.POST['location']
    # job.description = request.POST['description']
    job.save()
    return redirect("/home")

def projinv(request, id):
    user = User.objects.get(id=request.session['userid'])
    project = Project.objects.get(id=id)
    # my_investment = Project.objects.get(id=request.session['projectid'])
    # user.invested_projects.add(my_investment)
    context = {
        'user': user
    }
    return render(request, "investors.html", context)