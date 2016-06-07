from django.shortcuts import render
from shipdisplay.models import CrewDB
# Create your views here.
def base(request):
	title = 'Space Ship'
	context = {
		'title':title,
	}
	return render(request, "base.html", context)

def desktop(request):
    title = 'Desktop'
    crew = CrewDB.objects.all()
    context = {
        "title":title,
        "crew":crew,
    }
    return render(request,"desktop.html", context)