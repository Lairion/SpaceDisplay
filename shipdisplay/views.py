from django.shortcuts import render
from shipdisplay.models import CrewDB, PeopleDB
from django.http import HttpResponse
# Create your views here.
def base(request):
	title = 'Space Ship'
	context = {
		'title':title,
	}
	return render(request, "base.html", context)

def desktop(request):
    title = "Welcome"
    status = False
    context = {
        "title":title,
        "status":status
    }
    return render(request,"desktop.html", context)
    

def crew(request):
    if request.method == "GET":
        status = True
        window = request.GET['view']
        request.session['view'] = window
        if window == "Contact":
            title = "Contact Crew"
            context = {
                "title": title,
            }
        elif window == "Crew":
            title = window
            crew_list = CrewDB.objects.all()
            context = {
                "title": title,
                "crew_list":crew_list
            }
        elif window == "Storage":
            title = "Storage"
            context = {
                "title": title,
            }
        elif window == "Setting":
            title = "Setting"
            context = {
                "title": title,
            }
        elif window == "Drive":
            title = "Drive"
            context = {
                "title": title,
            }
        elif window == "Reasearch lab":
            title = "Reasearch lab"
            context = {
                "title": title,
            }
        elif window == "Sickbay":
            title = "Sickbay"
            context = {
                "title": title,
            }
        elif window == "About OS":
            title = "About OS"
            context = {
                "title": title,
            }
        else:
            title = "brocken"
            context = {
                "title": title,
            }
        return render(request,"desktop.html", context)

def description_crew(request):
    title = "Welcome"
    status = False
    context = {
        "title":title,
        "status":status
    }
    return render(request,"desktop.html", context)    
        
        