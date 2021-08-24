from django.shortcuts import redirect, render
from blog.forms import LoginModelForm, SignUpModelForm
from django.contrib import messages
from blog.views import blog_post_list_view


# Create your views here.
def login(request):
    form = LoginModelForm()
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
