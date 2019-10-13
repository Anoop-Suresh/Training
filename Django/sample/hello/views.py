from django.shortcuts import render
from django.http import HttpResponse
from hello.models import Student,Details,Mark
# Create your views here.


def home(request):

	name=Student.objects.order_by('Student_ID')
	name_dict={'NAME':name}

	return render(request,'hello.html',context= name_dict)