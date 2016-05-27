from django.shortcuts import render

# Create your views here.
def base(request):
	title = 'Space Ship'
	context = {
		'title':title,
	}
	return render(request, "base.html", context)

def desktop(request):
	title = 'Desktop'
	context = {
		"title":title,
	}
	return render(request,"desktop.html", context)