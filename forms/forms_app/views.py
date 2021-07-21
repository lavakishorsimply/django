from django.shortcuts import render
from forms_app.forms import Student
# Create your views here.
def stu_details(request):
    fm = Student()
    # fm = Student(label_suffix='>')

    return render(request,'home.html',{'form':fm})
