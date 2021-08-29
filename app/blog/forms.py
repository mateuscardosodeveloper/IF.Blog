from django import forms

from .models import BlogPost
from user.models import User
from comment.models import Comment


class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)


class LoginForm(forms.Form):

    email = forms.CharField(widget=forms.EmailInput(
        attrs={
        "class": "form-control"
    }))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password"
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email) # thisIsMyUsername == thisismyusername
        if not qs.exists():
            raise forms.ValidationError("This is an invalid email.")
        if qs.count() != 1:
            raise forms.ValidationError("This is an invalid email.")
        return email

class SignUpModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'slug', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def clean_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get("title")
        # iexact valid information if have uppercase or not
        queryset = BlogPost.objects.filter(title__iexact=title)
        if instance is not None:
            qs = queryset.exclude(pk=instance.pk)  # id=instance.pk
        if queryset.exists():
            raise forms.ValidationError(
                "This title has already been used. Please try again.")
        return title


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
