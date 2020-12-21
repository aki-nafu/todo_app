from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm, LoginForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from . forms import UserCreateForm
from django.views.generic import View
from django.contrib.auth.decorators import login_required

@login_required
def home(request):

    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            item = List(item=request.POST["item"],u_id=request.user.id)
            item.save()
            current_users_items=List.objects.filter(u_id=request.user.id)
            messages.success(request, ('Item Has Been Added To List'))
            return render(request, 'list.html', {'current_users_items': current_users_items})
    else:
        #all_items = List.objects.all
        current_users_items=List.objects.filter(u_id=request.user.id)
        return render(request, 'list.html', {'current_users_items': current_users_items})

@login_required
def about(request):
    context = {'first_name': 'Harry', 'last_name': 'Potter'}
    return render(request, 'about.html', context)

@login_required
def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item Has Been Deleted from List!'))
    return redirect('home')

@login_required
def uncomplete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')

@login_required
def complete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')

@login_required
def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            #all_items = List.objects.all
            current_users_items=List.objects.filter(u_id=request.user.id)
            messages.success(request, ('Item Has Been Edited!'))
            return redirect('home')
    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})


class Create_account(CreateView):
    def get(self, request, *args, **kwargs):
        #ここ
        form = UserCreateForm(request.POST)
        return  render(request, 'create_account.html', {'form': form,})
        
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            #フォームから'username'を読み取る
            username = form.cleaned_data.get('username')
            #フォームから'password1'を読み取る
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        return render(request, 'create_account.html', {'form': form,})
create_account = Create_account.as_view()

class Account_login(View):
    def post(self, request, *arg, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('/')
        return render(request, 'login.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'login.html', {'form': form,})

account_login = Account_login.as_view()

@login_required
def profile(request):

    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            current_users_items=List.objects.filter(u_id=request.user.id)
            
            messages.success(request, ('Item Has Been Added To List'))
            return render(request, 'list.html', {'current_users_items': current_users_items})
    else:
        current_users_items=List.objects.filter(u_id=request.user.id)
        return render(request, 'list.html', {'current_users_items': current_users_items})


    return render(request, 'list.html')