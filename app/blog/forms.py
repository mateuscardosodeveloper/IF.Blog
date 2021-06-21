from django import forms

from .models import BlogPost
from comment.models import Comment


class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)


class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'slug', 'content', 'publish_date']

    def clean_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get("title")
        queryset = BlogPost.objects.filter(title__iexact=title) #iexact valid information if have uppercase or not
        if instance is not None:
            qs = queryset.exclude(pk=instance.pk) #id=instance.pk
        if queryset.exists():
            raise forms.ValidationError("This title has already been used. Please try again.")
        return title


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']