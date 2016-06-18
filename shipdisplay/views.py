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
    if request.method == GET:
        window = request.GET['view']
        request.session['view'] = window
        if window == 'Connect':
            title = window
            crew_list = CrewDB.objects.all()
            for fk in crew_list:
                fks.append(CrewDB.objects.values_list("people_id",flat=True))
            context = {
                "title":title,
                "crew_list":crew_list,
                "fks" : fks,
                "count": count,
            }
            return render(request,"desktop.html", context)

def description_crew(request):
    if request.method == GET:
        request.session['view'] = True
        descript = request.GET['view']
        context = {
            "descript": descript,
        }
        
    else:
        descript = "Batman"
        context = {
            "descript": descript,
        }
        return render(request,"include/description_crew.html", context)
        