from django.shortcuts import redirect, render
from blog.forms import LoginModelForm, SignUpModelForm
from django.contrib import messages
from blog.views import blog_post_list_view
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

# Create your views here.
def login(request):
    form = LoginModelForm()   
    if form.is_valid():
        import ipdb;ipdb.set_trace()
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    #import ipdb;ipdb.set_trace()
    context = {'title': 'Logging', 'form': form}
    return render(request, "login.html", context)


def sing_up(request):
    form = SignUpModelForm(request.POST or None)
    if form.is_valid():
        try:
            obj = form.save(commit=False)
            obj.save(messages.success(request, "Registred successful"))
            return redirect(blog_post_list_view)
        except Exception:
            messages.add_message(request, messages.warning, 'Hello world.')
    context = {'title': 'Register', 'form': form}
    return render(request, "sign_up.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')
