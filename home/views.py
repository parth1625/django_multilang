from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils import translation


# Create your views here.
def index(request):
	if request.user.is_authenticated:
	    translation.activate(request.user.language)
	return render(request, 'home.html')