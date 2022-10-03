from django.shortcuts import render, redirect
from .forms import RegisterForm
# Create your views here.
def register(request, *args, **kwargs):
	if (request.method == "POST"):
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/aspp/home')
	else:
		form = RegisterForm()
		
	return render(request, "register/register.html", {
		"form":form
	})