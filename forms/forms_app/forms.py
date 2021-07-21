from django import forms
class Student(forms.Form):
    name = forms.CharField(max_length=70)
    age = forms.IntegerField()
    email = forms.EmailField()
    join_date = forms.DateField()
    address = forms.TextField()
