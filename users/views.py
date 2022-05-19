from django.shortcuts import render,redirect
from users.forms import UserRegisterForm
from django.contrib import messages


def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account for {username} created successfully')
            return redirect('home')
        else:
            messages.warning(request,f'Account not created')
            return redirect('register')
    else:
        form = UserRegisterForm()
        return render(request,'users/templates/register.html',{'form':form})


