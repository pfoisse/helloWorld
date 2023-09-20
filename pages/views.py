from django.http import HttpResponse

def homePageView(request):
    return HttpResponse("Hello world mon petit lapin rose !")
