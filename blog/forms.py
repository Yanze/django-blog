from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    """
    indicates which model to use to build the form in the Meta class
    of the form.

    Django introspects the model and builds the form dynamically for us.

    We can explicitly tell the framework which fields you want to exclude
    in yout form using a fields list. Or using exclude to exclude the list
    of fields.
    """
    class Meta:
        model = Comment  # inherits from Comment model
        fields = ('name', 'email', 'body')
