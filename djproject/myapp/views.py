from django.shortcuts import render
from .form import RegistrationForm1
from .form import LoginForm1,employeeForm
#import pyrebase
import datetime
from .models import tb_registration
from .models import employee
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound

def hello(request):
    text="<h1>hello welcome to site</h1>"
    return HttpResponse(text)
def hview(request):
    return render(request,"myapp/welcome.html")    #render function connects view to html page and returns response from middleware

today=datetime.datetime.now()
def t11(request):
    return render(request,"myapp/t1.html",{"name":"reetika","dat":today})
def order_demo(request):
    list=["pen","pencil","notebook"]
    uname="REETIKA"
    return render(request,"myapp/order.html",{"person_name":uname,"ship_date":today,"item_list":list})

def fur(request):
    return render(request,"myapp/body.html")
config={
"apiKey": "AIzaSyAsCCYhwuroCXZecRyAFDb3qYS7-GmSKjU",
"authDomain": "fproject-97fa3.firebaseapp.com",
"databaseURL": "https://fproject-97fa3.firebaseio.com",
"projectId": "fproject-97fa3",
"storageBucket": "fproject-97fa3.appspot.com",
"messagingSenderId": "73640965657",
"appId": "1:73640965657:web:7b8e9d26e5a4b704",
"type": "service_account",
"project_id": "fproject-97fa3",
"private_key_id": "974ba56f7cd258b5b2a3b62f889100ed1fbe165a",
"private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC4EKj56V7HSY1y\nE5DQqjjUFhrIOAUXatP2lqJbZ9okEHXp+WcZ9eoGHSXc6AIgJ7a2KpQvvioGij+M\ni5J6z1mUO2T0+F7SoXe0o1vjJcdAxv2RXRtOtpQaopr1PkJLKQGpXoxtyMhsTElO\nvAFBx4RKjIem/QjkuC64yVaGr8e/F2yIfzYpBPJXdE+8G14BmK4dlvGs8uqm+G9f\ns9z2eKRTg04VfVvre+ADrm5KIo2ilpj5HFF5tW5CY3rWpi++GAYt1Fji1YCX81/B\nk5Er8XFE/xDzs+iZ1+GaGm+mxOEA6sK3xJk2iFH+NjE2efHTQiCRY8E8+XH5KMHP\neJmMgqvlAgMBAAECggEAAXLSHZteTVOxGwV35Yh9Z3/gCJTWR2umDOH9F5qO3ytI\n/kUh8FSc2Zz3nBAwWhft6muV3HVS59fFLcI4biJ9GjtIbVwaBO7T3hZOBhDZS1N1\nkeQJb7pkmnwOm6D4jRZexroxgTisCRwllIrKuL2M9zg5ZhFGNWSUq4wcE/XErOaL\nG3lkmnZT35w3mmjkbjTDB6D4Z7crJ1bBFA9fX7+Q0VJeqbDfhXmmPRdaH9LLzyGl\ng5GxqJnkBPAYlor9U8MyaN2rEcNVdZ6SVJiSKmxjB/q2VZgKXdyDpUBCkCPMs7MB\nXTpwpITRq30rxAW8TqtwoOOyI5WAC1/vojus3B456QKBgQDvhIpRUerLnH1tZwHy\nZIEQr37AhvESCEujooL0PKRvV1xE7GrxMaOo4hDd5PC66vMfH4MS54KdouvpgMyi\nDPkmheSzhUHH5k4DDV9u06r2hL/+MWMzqUeVYeqsKM4DFpMG1r6kFCcDVhMJPmtN\nq2pLQgUKHg/vEDDJscpMOJ8LXQKBgQDEuz0zVnQy7A85YaJ/DA7vgjJ7gspxP4r1\nxiZk4ZFpx5GjQGIaJFqnMLWnoyfUfZYAgYPJp6RMbUbpPzoJaOM5d4B+EBFwfwBY\nhpZI0N2lIejMXxq/KfPwgjEYythLfQolPZGAA0CT3vDF10vnFnjBaoJQuxLk4Ujf\nVnw/SK2iKQKBgCMT6CXst1RGgOAK2/Ah4/0LlqafnKKlcF5wqHkYgISF6M93SFo2\niN9s7EdzBgZ57k06kjmsiiaH+8DgyhdZiwunRE0+UNnz0q0Dwlw6x6j+3BdgKEUi\nn4czJek8uJ8fKT0xKg5hnS0R6AvMhm6DkjefXZmTuYWre1mung/3ouNJAoGAO2+2\nVcRQ5vGax+NPjMK/4Gydg+NH9l8URJzRDLl5jVPWFFRnTy6clNaKi1MnvXMT1qNK\nhao4YT7CpcWMaztdKweHso54NlyoZhaDYQx5amKMSvKQyiCKqqcq3iqqnmPwpL+t\nLdfNst8wLxWUwQRxBz5+kJV0Z+IIejFO6G+0xcECgYEAvAMiwLmvVqGjWRQhIQGz\njVR8FBP6cLfjJWyI9gNVszz9ZsqnSJeqGF7GRLmnxVLuTa5am/etUpMq5l55Xcx+\niWn41KGQMIkCCDHqrNZmd76vkWCblgDz/BaMRHdlG13jQBMvA727gMDSIyJI53At\nSd06l2+Gi7QiET2/M/FHM3M=\n-----END PRIVATE KEY-----\n",
"client_email": "firebase-adminsdk-lmxv9@fproject-97fa3.iam.gserviceaccount.com",
"client_id": "100158580911851488850",
"auth_uri": "https://accounts.google.com/o/oauth2/auth",
"token_uri": "https://oauth2.googleapis.com/token",
"auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
"client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-lmxv9%40fproject-97fa3.iam.gserviceaccount.com"
}
#firebase = pyrebase.initialize_app(config)
#auth = firebase.auth()

# @@@@@@@@@@@@@  sessions @@@@@@@@@@@@@@@@@@@


def register(request):
    if request.method =='POST':
       # form = UserCreationForm(request.POST)
        form = RegistrationForm1(request.POST)
        if form.is_valid():
            #form.save()
            print("1111111111")
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            contact = form.cleaned_data["contact"]
            password = form.cleaned_data["password"]
            address = form.cleaned_data["address"]
            gender = form.cleaned_data["Gender"]
           # auth = firebase.auth()
            #user = auth.sign_in_with_email_and_password(email,password)
            p = tb_registration(name=name,email=email,contact=contact,address=address,gender=gender)
            p.save()
            print("/n/n this is valid data from the form ",gender)
            #return render(request,"myapp/Thanks.html",{"email":email,"password":password,"name":name,"contact":contact})
            return HttpResponseRedirect("myapp/Thanks.html")
        else:
            #form = UserCreationForm()
            #args = {'form':form}
            print("2222222222")
            return render(request,"myapp/reg.html",{'form':form})
    else:
        form = RegistrationForm1()
        #args = form
        print("2333333333")
        return render(request,"myapp/reg.html" ,{'form':form})

def Login(request):
    if request.method =="POST":
        data = request.POST #getting data from the form
        form = LoginForm1(data)
        if form.is_valid():
            u_email = form.cleaned_data["email"]
            u_password = form.cleaned_data["password"]
            p = tb_registration.objects.filter(email=u_email, password=u_password)
            print(p)
            # sessions
            if (p.count() > 0):
                print("valid user")
                request.session['username'] = u_email
                if request.session.has_key('username'):
                    name = request.session['username']
                print(name)
                return HttpResponseRedirect("/employee")
            else:
                print("try again")
                return HttpResponseNotFound('<h1> no page here </h1>')
        else:
            print("else block")
            return render(request, "myapp/loginn.html", {"form": form})
    else:
        form = LoginForm1()
        print("third else block")
        return render(request, "myapp/loginn.html", {"form": form})

def thanks(request):
    return render(request, "myapp/Thanks.html")

def employ(request):
    if request.method == "POST":
        data = request.POST #getting data from the form
        form = employeeForm(data)
        if form.is_valid():
            #ename1 = form.cleaned_data["ename"]
            Job_title1 = form.cleaned_data["Job_title"]
            Specialization1 = form.cleaned_data["Specialization"]
            experience1 = form.cleaned_data["experience"]
            if request.session.has_key('username'):
                print("hi")
                n = request.session['username']
            q = tb_registration.objects.filter(email = n)
            q = list(q)
            tup = q[0]
            print(n)
            p1 = employee(email1 = tup,Job_title=Job_title1,Specialization=Specialization1,experience= experience1 )
            p1.save()
            #print("/n/n this is valid data from the form ", gender)
            # return render(request,"myapp/Thanks.html",{"email":email,"password":password,"name":name,"contact":contact})
            return HttpResponseRedirect("/Thanks")
        else:
            # form = UserCreationForm()
            # args = {'form':form}
            print("2222222222")
            return render(request, "myapp/employee.html", {'form': form})
    else:
        form = employeeForm()
        # args = form
        print("2333333333")
        return render(request, "myapp/employee.html", {'form': form})


def temp(request):
    return render(request, "myapp/index.html")
def inh(request):
    return render(request,"myapp/inherittt.html")



