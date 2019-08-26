from django.shortcuts import render

# Create your views here.
def hello1(request):
    text="<h1>hello welcome to site</h1>"
    return HttpResponse(text)
def hview1(request):
    return render(request,"myapp/welcome.html")
