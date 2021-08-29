from django.shortcuts import redirect, render
from blog.forms import LoginForm, SignUpModelForm
from django.contrib import messages
from blog.views import blog_post_list_view
from django.contrib.auth import logout, authenticate, login


def login_view(request):
    form = LoginForm(request.POST or None)   
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, email=email, password=password)
        if user != None:
            login(request, user)
            return redirect('/')
        else:
            request.session['invalid_user'] = 1
    #import ipdb;ipdb.set_trace()
    context = {'title': 'Logging', 'form': form}
    return render(request, "login.html", context)


def sing_up(request):
    form = SignUpModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save(messages.success(request, "Registred successful"))
        return redirect(blog_post_list_view)
    context = {'title': 'Register', 'form': form}
    return render(request, "sign_up.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')
