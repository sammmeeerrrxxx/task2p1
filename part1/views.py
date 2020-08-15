from django.shortcuts import render,redirect
from .models import user
from django.http import HttpResponse
# Create your views here.
def register(request):
	if request.method == 'GET':
		return render(request, 'part1/register.html')

	elif request.method == 'POST':
		profile = user(firstname=request.POST.get("firstname"),lastname=request.POST.get("lastname"),
			phoneno=request.POST.get("phoneno"),email=request.POST.get("email"),
			gender=request.POST.get("gender"))
		profile.save()
		return render(request,'part1/result.html', {'error':"User has been succesfully registered.",'user':''})


def find(request):
	if request.method == 'GET':
		return render(request, 'part1/find.html')


	elif request.method == 'POST':
		user1 = user.objects.filter(email=request.POST.get('email'))
		if user1:
			context = {'user': user1, 'error':'Found User!'}
			return render(request, 'part1/result.html', context)
		else:
			
			return render(request, 'part1/result.html',{"error":"Sorry user not found.",'user':''})