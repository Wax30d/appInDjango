from django.http import HttpResponse


def index(request):
    return HttpResponse("Django Tutorial by Wax30d<html><body><h1> Hello World Django tutorials Tour</body></html>")
