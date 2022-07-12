import django
from django.shortcuts import redirect, render
from requests import session
from .models import Accounts, Pro, VendorAcc
from django.db.models import Q

# Create your views here.

def signupview(request):
    if request.method=='POST':
        model=Accounts()
        model.fullname=request.POST['fullname']
        model.email=request.POST['email']
        model.password=request.POST['password']
        model.birth=request.POST['bdate']
        model.save()
        request.session['user']=model.id
        return redirect('homeview')

    return render(request, 'signupview.html', {'k':'Login'})

def loginview(request):
    msg=''
    if request.method=='POST':
        try:
            m=Accounts.objects.get(email=request.POST['email'])

            if m.password==request.POST['password']:
                request.session['user']=m.id
                return redirect('homeview')
            else:
                msg='Invalid Credentials!'
        except:
            msg='Invalid Credentials!'

    return render(request, 'loginview.html', {'k': 'Signup', 'msg': msg})

def homeview(request):
    if 'user' in request.session.keys():
        d=Pro.objects.all()
        if request.GET.get('search'):
            d=searchview(request)
        return render(request, 'homeview.html', {'k':'Signup', 'd':d})
    else:
        return redirect('loginview')

def prodelete(request, abc):
    d=Pro.objects.get(id=abc)
    d.delete()
    return redirect('vendorinventoryview')

def searchview(request):
    try:
        q=request.GET.get('search')
    except:
        q=None
    if q:
        pros=Pro.objects.filter(Q(title__icontains=q) | Q(desc__icontains=q) | Q(price__icontains=q))
    else:
        pros=None
    return pros

def productview(request,abc):
    d=Pro.objects.get(id=abc)
    return render(request, 'productview.html', {'d':d})

def logout(request):
    if 'user' in request.session.keys():
        del request.session['user']
        return redirect('loginview')
    else:
        return redirect('loginview')

def vendorloginview(request):
    msg=''
    if request.method=='POST':
        try:
            m=VendorAcc.objects.get(email=request.POST['email'])

            if m.password==request.POST['password']:
                request.session['vendor']=m.id
                return redirect('vendorinventoryview')
            else:
                msg='Invalid Credentials!'
        except:
            msg='Invalid Credentials!'
    return render(request, 'vendorloginview.html', { 'msg': msg})

def vendorinventoryview(request):
    if 'vendor' in request.session.keys():
        try:
            d=Pro.objects.filter(v_id=request.session['vendor'])
        except:
            d=None
        if request.GET.get('search'):
            d=searchview(request)

        if request.method=='POST':
            model=Pro()
            model.title=request.POST['prtitle']
            model.desc=request.POST['prdesc']
            model.price=request.POST['prprice']
            model.ratting=request.POST['prratting']
            model.image = request.FILES.get('primage') # for image upload enctype="multipart/form-data"
            model.v_id=request.session['vendor']
            model.save()
            return redirect('vendorinventoryview')

    else:
         return redirect('vendorloginview')

    return render(request, 'vendorinventoryview.html', { 'd':d })


def vendorlogout(request):
    if 'vendor' in request.session.keys():
        del request.session['vendor']
        return redirect('vendorloginview')
    else:
        return redirect('vendorloginview')

    # if 'user' in request.session.keys():
    #     d=Pro.objects.all()
    #     if request.GET.get('search'):
    #         d=searchview(request)
    #     return render(request, 'homeview.html', {'k':'Signup', 'd':d})
    # else:
    #     return redirect('loginview')