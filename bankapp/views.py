from django.http import JsonResponse
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import PersonalInformation, District, Branch
from django.contrib import messages
from .forms import YourForm



def index(request):
    return render(request, "index.html")

def member(request):
    return render(request, "member.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('bankapp:index')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('bankapp:login')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken")
                return redirect('bankapp:register')
            else:
                user = User.objects.create_user(username=username, password=password)
                # personal_info = PersonalInformation(username=user)  # This line causes the error
                user.save()
                messages.success(request, "User created successfully")
                return redirect('bankapp:login')
        else:
            messages.error(request, "Passwords do not match")
            return redirect('bankapp:register')
    return render(request, "register.html")

def logout_view(request):
    auth.logout(request)
    return redirect('bankapp:index')

def next(request):
    return render(request, "index.html")

def next1(request):
    return render(request, "https://www.google.co.in/")


def account_registration(request):
    if request.method == 'POST':
        form = YourForm(request.POST)
        if form.is_valid():
            personal_info = form.save(commit=False)
            personal_info.user = request.user
            personal_info.save()
            messages.success(request, "Account registered successfully")
            return redirect('bankapp:index')
        else:
            messages.error(request, "Error in the form. Please correct the errors.")
    else:
        form = YourForm()

    districts = District.objects.all()
    branches_by_district = {district.name: Branch.objects.filter(district=district) for district in districts}

    return render(request, 'member.html', {'form': form, 'districts': districts, 'branches_by_district': branches_by_district})


def get_branches(request):
    district_id = request.GET.get('district_id', None)
    if district_id:
        branches = Branch.objects.filter(district_id=district_id)
        branch_list = [{'id': branch.id, 'name': branch.name} for branch in branches]
        return JsonResponse({'branches': branch_list})

    return JsonResponse({'branches': []})

