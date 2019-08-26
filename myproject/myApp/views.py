from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .form import signinForm
from .form import TrainerSignInForm
def hello(request):
    text = "<h1> welcome </h1>"
    return HttpResponse(text)

def Login(request):
    return render(request, "myApp/Login.html")

def thanks(request):
    return render(request, "myApp/Thanks.html")

def signin(request):
    if request.method == "POST":
        data = request.POST #getting data from the form
        form = signinForm(data)
        if form.is_valid():
            rgid = form.cleaned_data["rgid"]
            return HttpResponseRedirect("myApp/Thanks.html")
        else:
            # form = UserCreationForm()
            # args = {'form':form}
            print("2222222222")
            return render(request, "myApp/signin.html", {'form': form})
    else:
        form = signinForm()
        #args = form
        print("2333333333")
        return render(request,"myApp/signin.html" ,{'form':form})


def TrainerSignIn(request):
    if request.method == "POST":
        data = request.POST #getting data from the form
        form = TrainerSignInForm(data)
        if form.is_valid():
            empID = form.cleaned_data["empID"]
            password = form.cleaned_data["password"]
            return HttpResponseRedirect("/Thanks")
        else:
            print("2222222222")
            return render(request, "myApp/TrainerSignIn.html", {'form': form})
    else:
        form = TrainerSignInForm()
        print("2333333333")
        return render(request,"myApp/TrainerSignIn.html" ,{'form':form})



