from django.shortcuts import render,get_object_or_404, redirect
from .forms import Places, PlacesForm
from travello.models import Destination
from django.http import HttpResponse

def mainPage(request):
	dests = Destination.objects.all()
	return render(request, "manage.html", {'dests': dests})

def addPlace(request):
	form = Places() #request.GET
	if request.method == "POST":
		form = Places(request.POST, request.FILES)
		if form.is_valid():
			print(form.cleaned_data)
			Destination.objects.create(**form.cleaned_data)
			return redirect('../managePlaces/mainPage')
		else:
			print(form.errors)
	context = {
		'form' : form,
	}
	return render(request, "managePlaces.html", context)

def updatePlace(request,theid):
	obj = Destination.objects.get(id = theid)
	form = PlacesForm(request.POST or None,  instance = obj)
	if form.is_valid():
		if bool(request.FILES.get('img',False)) == True:
			obj.img = request.FILES['img']
		form.save()
		form = PlacesForm()
		return redirect('../../mainPage')
	context = {
		'form': form,
	}
	return render(request, "managePlaces.html", context)

def deletePlace(request,theid):
	obj = get_object_or_404(Destination, id = theid)
	if request.method == 'POST':
		print("Lo borro")
		obj.delete()
		return redirect('../../mainPage')
	context = {
		'obj': obj,
	}
	return render(request, "deletePlace.html", context)
