from django.shortcuts import render
from shipdisplay.models import CrewDB, PeopleDB
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
            
            
    return render(request,"desktop.html", context)


def crew(request):
    title = 'Crew'
    crew_list = CrewDB.objects.all()
    context = {
        "title":title,
        "crew_list":crew_list,
    }
    return render(request,"page/crew.html", context)
    
        