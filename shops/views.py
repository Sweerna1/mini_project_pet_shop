from django.shortcuts import render, redirect
from .models import Pet
from .forms import PetForm, SignupForm, SigninForm
from django.contrib.auth import login, authenticate, logout

def no_access(request):
	context = {
	"message":"NO WAY!"
	}
	return render(request, 'noaccess.html',context)


def signup(request):
	form = SignupForm()
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)

			user.set_password(user.password)
			user.save()

			login(request, user)
			return redirect("pet-list")
	context = {
		"form":form,
	}
	return render(request, 'signup.html', context)


def signin(request):
	form = SigninForm()
	if request.method == 'POST':
		form = SigninForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			auth_user = authenticate(username=username, password=password)
			if auth_user is not None:
				login(request, auth_user)
				return redirect('pet-list')
	context = {
		"form":form
	}
	return render(request, 'signin.html', context)

def signout(request):
	logout(request)
	return redirect("pet-list")



#############################
def pet_list(request):

    context = {
        "pets":Pet.objects.filter(available=True)
    }
    return render(request, 'list.html', context)


def pet_detail(request, pet_id):

    pet = Pet.objects.get(id=pet_id)
    context = {
        "pet": pet,
    }
    return render(request, 'detail.html', context)

######################################
def pet_create(request):
    if request.user.is_anonymous:
        return redirect('signin')
    form = PetForm()
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pet-list')
    context = {
        "form":form,
    }
    return render(request, 'create.html', context)



def pet_update(request, pet_id):
	pet_obj = Pet.objects.get(id=pet_id)

	if not request.user.is_staff:
		return redirect('no-access')

	form = PetForm(instance=pet_obj)
	if request.method == "POST":
		form = PetForm(request.POST, request.FILES, instance=pet_obj)
		if form.is_valid():
			form.save()
			return redirect('pet-detail', pet_id=pet_obj.id)
	context = {
	"pet_obj": pet_obj,
	"form":form,
	}
	return render(request, 'update.html', context)



def pet_delete(request, pet_id):
    pet_obj = Pet.objects.get(id=pet_id)
    if not request.user.is_staff:
        return redirect('no-access')
    pet_obj.delete()
    return redirect('pet-list')


