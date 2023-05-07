from django.shortcuts import render,redirect
import socket
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from .auth_backends import CustomBackend
from django.contrib.sessions.models import Session
from django.http import HttpResponse  

# Create your views here.
def Index(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'about.html')

def Track(request):
    return render(request, 'chart.html')

def Profile(request,pk):
    if request.user.is_authenticated:
        user=User.objects.get(id=pk)
        context={
            'pdb':user,
        }
        return render(request,"profile.html",context)
    else:
        return redirect("login")


def signup(request):
    user = request.user
    if request.user.is_authenticated:
        return redirect("signup")
    context = {}
    try:
        if request.method == 'POST':
            fname=request.POST.get("first_name")
            lname=request.POST.get("last_name")
            email=request.POST.get("email")
            username=request.POST.get("username")
            password1=request.POST.get("password1")
            password2=request.POST.get("password2")

            # print("Than correct!")
            if User.objects.filter(username=username).first():
                messages.error(
                    request, "This username is already taken! Please login with user id!")
                return redirect('signup')
            if User.objects.filter(email=email).first():
                messages.error(
                    request, "This email is already taken! Please login with user id")
                return redirect('signup')
            if password1 == password2:
                fname=request.POST.get("first_name")
                lname=request.POST.get("last_name")
                email=request.POST.get("email")
                username=request.POST.get("username")
                password1=request.POST.get("password1")
                password2=request.POST.get("password2")

                user = User.objects.create_user(
                    username=username, email=email, password=password1, first_name=fname, last_name=lname)
                user.save()
                
                # login(request, user)
                # messages.success(request, "Welcome {}".format(
                    # request.user.get_short_name()))
                
                return redirect("login")
            else:
                messages.warning(request, 'Password must be same!')
                return render(request, "signup.html", context)
        else:
            return render(request, "signup.html", context)
    except socket.gaierror:
        return HttpResponseServerError("Internet connection error")
 
    
def Login(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == 'POST':
        username = request.POST.get('username')
        
        password = request.POST.get('password')
      
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"Login Successfully!!")
            return redirect("home")
        else:
            messages.warning(request,"User or password is not correct!")

    return render(request, "login.html")




def Logout(request):
    logout(request)
    return redirect('home')

def feature(request):
    return render(request, 'feature.html')
    
def Error(request):
    return render(request, '404.html')
def profile(request):
    return render(request, 'profile.html')

def exchange(request):
    return render(request, 'exchange.html' )

def crypto(request):
    return render(request, 'crypto.html' )

def aboutcrypto(request):
    return render(request, 'aboutcrypto.html')





class CustomLoginView(LoginView):
    template_name = 'login.html'
    # authentication_form = CustomAuthenticationForm
    success_url = reverse_lazy('home')
    redirect_authenticated_user = True
    authentication_backend = CustomBackend()

    def form_valid(self, form):
        user = form.get_user()
        auth_login(self.request, user)
        return self.authentication_backend.login_success_redirect(self.request, user)
    
  

def my_view(request):
    # Read a session variable
    my_var = request.session.get('my_var_name')

    # Write a session variable
    request.session['my_var_name'] = 'my_var_value'

    # Delete a session variable
    del request.session['my_var_name']

    # Get the session ID
    session_id = request.session.session_key

    # Get the session object (using the session ID)
    session = Session.objects.get(session_key=session_id)
    return render(request, 'index.html')


        


    
    
