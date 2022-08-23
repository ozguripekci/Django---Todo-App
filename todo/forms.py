from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = '__all__' 
        # labels = {"first_name": "Name", "last_name":"Surname", "number":"Number"}