from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.core.paginator import Paginator
from django.urls import reverse
from django.contrib.auth import authenticate ,logout 
from django.contrib.auth import login as mylogin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
import re


@login_required(login_url='login')
def home(request):
    return render(request,'home.html')

@login_required(login_url='login')
def clients(request):
    clients=Client.objects.all()
    paginator = Paginator(clients, 8)
    page = request.GET.get('page')
    clients = paginator.get_page(page)
    return render(request,'client/clients.html',{'clients':clients})

@login_required(login_url='login')
def client(request,pk):
    credits=Credit.objects.filter(client=pk)
    paginator = Paginator(credits, 8)
    page = request.GET.get('page')
    credits = paginator.get_page(page)
    client=Client.objects.get(id=pk)
    return render(request,'client/client.html',{'client':client,'credits':credits})
@login_required(login_url='login')
def clientunpaid(request,pk):
    credits=Credit.objects.filter(client=pk,status='unpaid')
    paginator = Paginator(credits, 8)
    page = request.GET.get('page')
    credits = paginator.get_page(page)
    client=Client.objects.get(id=pk)
    return render(request,'client/client.html',{'client':client,'credits':credits})
@login_required(login_url='login')
def clientpaid(request,pk):
    credits=Credit.objects.filter(client=pk,status='paid')
    paginator = Paginator(credits, 8)
    page = request.GET.get('page')
    credits = paginator.get_page(page)
    client=Client.objects.get(id=pk)
    return render(request,'client/client.html',{'client':client,'credits':credits})
@login_required(login_url='login')
def creditupdatestatus(request,pk):
    credit = Credit.objects.get(id=pk)
    clientid= credit.client.id
    data ={
    'clientid': credit.client.id,
    'clientFirstname': credit.client.firstName,
    'clientLastname': credit.client.lastName,
    'produitname': credit.produit.title,
    'creditdate': credit.date_created,
    }
    form = CreditUpdate(instance=credit)
    if request.method == 'POST':
        form=CreditUpdate(request.POST,instance=credit)
        if form.is_valid():
            form.save()
            client_detail_url = reverse('client', args=[clientid])
            return redirect(client_detail_url)
    context = {'form': form, 'data': data}
    return render(request,'credit/creditupdateform.html',context)
@login_required(login_url='login')
def clientCreate(request):
    form=ClientForm()
    if request.method == 'POST':
        form=ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/clients')
    context={'form':form}
    return render(request,'client/clientForm.html',context)
@login_required(login_url='login')
def clientupdate(request,pk):
    client = Client.objects.get(id=pk)
    form = ClientForm(instance=client)
    if request.method == 'POST':
        form=ClientForm(request.POST,instance=client)
        if form.is_valid():
            form.save()
            return redirect('/clients')
    context={'form':form}
    return render(request,'client/clientForm.html',context)
@login_required(login_url='login')
def clientdelete(request,pk):
    client = Client.objects.get(id=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('/clients')
    context={'form':client}
    return render(request,'client/deleteclient.html',context)

@login_required(login_url='login')
def produits(request):
    produits=Produit.objects.all()
    paginator = Paginator(produits, 8)
    page = request.GET.get('page')
    produits = paginator.get_page(page)
    return render(request,'produit/produits.html',{'produits':produits})
def produitCreate(request):
    form=ProduitForm()
    if request.method == 'POST':
        form=ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/produits')
    context={'form':form}
    return render(request,'produit/produitForm.html',context)
@login_required(login_url='login')
def produitupdate(request,pk):
    produit = Produit.objects.get(id=pk)
    form = ProduitForm(instance=produit)
    if request.method == 'POST':
        form=ProduitForm(request.POST,instance=produit)
        if form.is_valid():
            form.save()
            return redirect('/produits')
    context={'form':form}
    return render(request,'produit/produitForm.html',context)
@login_required(login_url='login')
def produitdelete(request,pk):
    produit = Produit.objects.get(id=pk)
    if request.method == 'POST':
        produit.delete()
        return redirect('/produits')
    context={'form':produit}
    return render(request,'produit/deleteproduit.html',context)

@login_required(login_url='login')
def credits(request):
    credits=Credit.objects.all()
    unpaid_sum = Credit.objects.filter(status='unpaid').aggregate(Sum('produit__price'))
    unpaid_sum = unpaid_sum['produit__price__sum']
    paid_sum = Credit.objects.filter(status='paid').aggregate(Sum('produit__price'))
    paid_sum = paid_sum['produit__price__sum']
    total_sum = Credit.objects.all().aggregate(Sum('produit__price'))
    total_sum = total_sum['produit__price__sum']
    paginator = Paginator(credits, 8)
    page = request.GET.get('page')
    credits = paginator.get_page(page)
    data={
    'unpaid_sum':unpaid_sum,
    'paid_sum':paid_sum,
    'total_sum':total_sum, 
    }
    context={'credits':credits,'data':data}
    return render(request,'credit/credits.html',context)
@login_required(login_url='login')
def creditunpaid(request):
    credits=Credit.objects.filter(status='unpaid')
    unpaid_sum = Credit.objects.filter(status='unpaid').aggregate(Sum('produit__price'))
    unpaid_sum = unpaid_sum['produit__price__sum']
    paid_sum = Credit.objects.filter(status='paid').aggregate(Sum('produit__price'))
    paid_sum = paid_sum['produit__price__sum']
    total_sum = Credit.objects.all().aggregate(Sum('produit__price'))
    total_sum = total_sum['produit__price__sum']
    paginator = Paginator(credits, 8)
    page = request.GET.get('page')
    data={
    'unpaid_sum':unpaid_sum,
    'paid_sum':paid_sum,
    'total_sum':total_sum, 
    }
    credits = paginator.get_page(page)
    context={'credits':credits,'data':data}
    return render(request,'credit/credits.html',context)
@login_required(login_url='login')
def creditpaid(request):
    credits=Credit.objects.filter(status='paid')
    unpaid_sum = Credit.objects.filter(status='unpaid').aggregate(Sum('produit__price'))
    unpaid_sum = unpaid_sum['produit__price__sum']
    paid_sum = Credit.objects.filter(status='paid').aggregate(Sum('produit__price'))
    paid_sum = paid_sum['produit__price__sum']
    total_sum = Credit.objects.all().aggregate(Sum('produit__price'))
    total_sum = total_sum['produit__price__sum']
    paginator = Paginator(credits, 8)
    page = request.GET.get('page')
    data={
    'unpaid_sum':unpaid_sum,
    'paid_sum':paid_sum,
    'total_sum':total_sum, 
    }
    credits = paginator.get_page(page)
    context={'credits':credits,'data':data}
    return render(request,'credit/credits.html',context)
@login_required(login_url='login')
def creditCreate(request):
    form=CreditForm()
    if request.method == 'POST':
        form=CreditForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/credits')
    context={'form':form}
    return render(request,'credit/creditForm.html',context)
@login_required(login_url='login')
def creditupdate(request,pk):
    credit = Credit.objects.get(id=pk)
    form = CreditForm(instance=credit)
    if request.method == 'POST':
        form=CreditForm(request.POST,instance=credit)
        if form.is_valid():
            form.save()
            return redirect('/credits')
    context={'form':form}
    return render(request,'credit/creditForm.html',context)
@login_required(login_url='login')
def creditdelete(request,pk):
    credit = Credit.objects.get(id=pk)
    if request.method == 'POST':
        credit.delete()
        return redirect('/credits')
    context={'form':credit}
    return render(request,'credit/deletecredit.html',context)

@login_required(login_url='login')
def register(request):
    form = CreateNewUser()
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form':form}
    return render(request,'register.html',context)

def userLogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                mylogin(request,user)
                return redirect('home')
            else:
                messages.info(request,'credentials error')
    context = {}
    return render(request,'login.html',context)

def userlogout(request):
    logout(request)
    return redirect('login')

# emel bottonat d show unpaid w show paid , w show credit by client