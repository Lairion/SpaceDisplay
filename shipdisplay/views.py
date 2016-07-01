from django.shortcuts import render
from shipdisplay.models import CrewDB, PeopleDB
from django.http import HttpResponse, HttpResponseRedirect, Http404
# Create your views here.
def base(request):
	title = 'Space Ship'
	context = {
		'title':title,
	}
	return render(request, "base.html", context)

def desktop(request):
    title = "Welcome"
    context = {
        "title": title, 
    }
    if request.method = "GET":
        if request.GET['view'] == "Galaxy map":
            return HttpResponseRedirect()
            
        else if request.GET['view'] == "Galaxy map":
        else if request.GET['view'] == "Spaceship":
        else if request.GET['view'] == "Connect":
        else if request.GET['view'] == "Crew":
        else if request.GET['view'] == "Storage":
        else if request.GET['view'] == "Setting":
        else if request.GET['view'] == "Drive":
        else if request.GET['view'] == "Research lab":
        else if request.GET['view'] == "Sickbay":
        else if request.GET['view'] == "About OS":
            
            
    return render(request,"desktop.html", context)


def crew(request):
    title = 'Crew'
    crew_list = CrewDB.objects.all()
    context = {
        "title":title,
        "crew_list":crew_list,
    }
    return render(request,"page/crew.html", context)
    
        