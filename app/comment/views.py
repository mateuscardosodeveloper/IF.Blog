from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from blog.forms import CommentModelForm
from blog.models import BlogPost


# Create your views here.

@login_required
def comment_view(request, slug):
    slug = get_object_or_404(BlogPost, slug=slug)
    form = CommentModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.blogpost = slug
        obj.save(messages.success(request, "Commented post."))
        return redirect('/blog')
    template_name = 'form.html'
    context = {'title': f'Commenting the post - {slug.title}' , 'form': form}
    return render(request, template_name, context)
