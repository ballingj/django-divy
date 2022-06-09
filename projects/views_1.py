from django.shortcuts import render
from django.http import HttpResponse

# Rendering data to Templates

def projects(request):
    msg = "You are on the projects page"
    number = 2
    context = {'message': msg, 'number': number}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    return render(request, 'projects/single-project.html')
    #return HttpResponse('<h2>' + 'Single Project' + ' ' + str(pk))
