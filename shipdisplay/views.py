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
    title = 'Desktop'
    crew_list = CrewDB.objects.all()
    count = len(crew_list) - 1
    fks = []
    for fk in crew_list:
        fks.append(CrewDB.objects.values_list("people_id",flat=True))
        print fks
    context = {
        "title":title,
        "crew_list":crew_list,
        "fks" : fks,
        "count": count,
    }
    return render(request,"desktop.html", context)

def description_crew(request):
    if request.method == 'GET':
        status = True;
        descript = PeopleDB.objects.get(pk=request.session["view"])
        context = {
            "status": status,
            "descript": descript,
        }
        return render(request,"include/description_crew.html", context)
    else:
        status = False
        context = {
            "status": status,
        }
        return render(request,"include/description_crew.html", context)
        