from django.shortcuts import render, redirect
from bankapp.forms import UserForm, UserInfoForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *

# from .decorator import kyc_complete

# Create your views here.


def home_page(request):
    if request.user.is_authenticated:
        return redirect ("dashboard")
    else:
        return render(request, 'account/home-page.html')

def register(request):
    if request.user.is_authenticated:
            return redirect('login')         
    form=UserForm()
    if request.method =='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            form.save()
            messages.success(request,'Account was created for '+email)
            return redirect('login')
        else:
            form=UserForm()
            messages.error(request,'Something went wrong')
            context={'form':form}
            return render(request,"account/register.html", context)
    else:
        form=UserForm()
        context={'form':form}
        return render(request,"account/register.html",context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method=='POST':
            email=request.POST.get('email')
            password= request.POST.get('password')
            user=authenticate(request,email=email,password=password)

            if user is not None:
                login(request, user)
                messages.success(request,'Login Successful')
                return redirect('dashboard')
            else:
                messages.error(request,'Error! Invalid credential')
                return render(request,"account/login.html")

        else:  
            return render(request, "account/login.html")
            
@login_required
def signout(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    user = request.user
    kyc=UserInfo.objects.get(user=user)
    account = Account.objects.get(user=user)
    
    if kyc.is_kyc_complete == False:
        messages.info(request, "You need to Complete your KYC")
        return redirect ('kyc')    
    
    context = {
        "kyc":kyc,
        "account": account
    }
    return render (request, "account/dashboard.html", context)

@login_required
def kyc_registration(request):
    user = request.user 
    kyc = UserInfo.objects.get(user=user)

    if request.method == "POST":
        form=UserInfoForm(request.POST, request.FILES, instance=kyc)
        if form.is_valid():
            kyc.is_kyc_complete = True
            kyc.full_name = form.cleaned_data["full_name"]
            kyc.gender = form.cleaned_data["gender"]
            kyc.marital = form.cleaned_data["marital"]
            kyc.phone_number = form.cleaned_data["phone_number"]
            kyc.state = form.cleaned_data['state']
            kyc.lga = form.cleaned_data['lga']
            kyc.residential_address = form.cleaned_data['residential_address']
            kyc.identity_type=form.cleaned_data['identity_type']
            kyc.identity_image = form.cleaned_data['identity_image']
            kyc.passport=form.cleaned_data['passport']
            kyc.date_of_birth=form.cleaned_data['date_of_birth']
            kyc.signature = form.cleaned_data['signature']
            kyc.next_of_kin=form.cleaned_data['next_of_kin']
            kyc.kin_number = form.cleaned_data['kin_number']
            kyc.save()
            return redirect('info')
        else:
            messages.error(request, 'Error Detected')
            return redirect('kyc')
    else:
        form=UserInfoForm(instance=kyc)
    context = {
         'form':form,
         'kyc':kyc,
               }
    return render(request, 'account/kyc.html', context)


def account_info(request):
    user = request.user
    account = Account.objects.get(user=user)

    context={
        'account':account
    }
    return render(request, 'account/account-info.html', context)


@login_required
def transfer_view(request):
    user = request.user
    sender_account = Account.objects.get(user=user)
    if request.method == "POST":
        
        receiver_account_number = request.POST.get("receiver_account_number")
        amount = int(request.POST.get("amount"))
        pin = int(request.POST.get("pin"))
        description = request.POST.get("description")

        try:
            if pin == sender_account.pin_number:
                receiver_account = Account.objects.get(account_number=receiver_account_number)
                sender_account.account_balance -= amount
                sender_account.save()
                receiver_account.account_balance+= amount
                receiver_account.save()
                Transaction.objects.create(sender=sender_account, receiver=receiver_account, amount=amount, description=description)
                messages.success(request, 'Transfer Successful')
            else:
                messages.error(request, 'Incorrect Pin')
                return redirect (request.path)

        except Account.DoesNotExist:
            messages.error(request, 'Account does not exist')
            return redirect (request.path)
            
    return render(request, "account/transfer.html")