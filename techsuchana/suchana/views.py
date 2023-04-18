from django.shortcuts import render,get_object_or_404
from .models import TechSuchana
from django.db.models import Q


# Create your views here.
def detailnews(request,id):
    obj = get_object_or_404(TechSuchana,pk=id)
    latest = TechSuchana.objects.filter(latest=True).order_by('-created_date')[:5]
    return render(request,'suchana_html/detail.html',{'obj':obj,'latest':latest})

def getnews(request):
    home=TechSuchana.objects.filter(home = True).order_by('-created_date')[0]
    latest = TechSuchana.objects.filter(latest=True).order_by('-created_date')[:5]
    technews = TechSuchana.objects.filter(technews=True).order_by('-created_date')[:6]
    automobile = TechSuchana.objects.filter(automobile=True).order_by('-created_date')[:6]
    techsiksha = TechSuchana.objects.filter(techsiksha=True).order_by('-created_date')[:6]
    techdeals = TechSuchana.objects.filter(techdeals=True).order_by('-created_date')[:6]
    cybercrime = TechSuchana.objects.filter(cybercrime=True).order_by('-created_date')[:6]
    for field in TechSuchana._meta.fields:
        print(field.get_attname_column())
    print(latest)
    print(technews)
    print(automobile)
    return render(request,'suchana_html/base.html',{'home':home ,'latest':latest,'technews':technews,'automobile':automobile,'techsiksha':techsiksha,'techdeals':techdeals,'cybercrime':cybercrime})

def gettechnews(request):
    technews = TechSuchana.objects.filter(technews=True).order_by('-created_date')
    return render(request,'suchana_html/catagory.html',{'news':'TechNews','technews':technews})

def getautomobile(request):
    automobile = TechSuchana.objects.filter(automobile=True).order_by('-created_date')
    return render(request,'suchana_html/catagory.html',{'news':'Automobile','technews':automobile})

def gettechsiksha(request):
    techsiksha = TechSuchana.objects.filter(techsiksha=True).order_by('-created_date')
    return render(request,'suchana_html/catagory.html',{'news':'TechEducation','technews':techsiksha})

def gettechdeals(request):
    techdeals = TechSuchana.objects.filter(techdeals=True).order_by('-created_date')
    return render(request,'suchana_html/catagory.html',{'news':'TechDeals','technews':techdeals})

def getcybercrime(request):
    cybercrime = TechSuchana.objects.filter(cybercrime=True).order_by('-created_date')
    return render(request,'suchana_html/catagory.html',{'news':'CyberCrime','technews':cybercrime})

def getinternet(request):
    internet = TechSuchana.objects.filter(internet=True).order_by('-created_date')
    return render(request,'suchana_html/catagory.html',{'news':'Internet','technews':internet})

def gettechjobs(request):
    techjobs = TechSuchana.objects.filter(techjobs=True).order_by('-created_date')
    return render(request,'suchana_html/catagory.html',{'news':'TechJobs','technews':techjobs})

def getgadgets(request):
    gadgets = TechSuchana.objects.filter(gadgets=True).order_by('-created_date')
    return render(request,'suchana_html/catagory.html',{'news':'Gadgets','technews':gadgets})

def search(request):
    results=[]
    if request.method=='GET':
        query=request.GET.get('search')
        results=TechSuchana.objects.filter(Q(headlines__icontains=query) | Q(news__icontains=query))
    return render(request,'suchana_html/catagory.html',{'query':query,'news':'Search Results','technews':results})

def getpolicy(request):
    return render(request,'suchana_html/privacypolicies.html')

def getaboutus(request):
    return render(request,'suchana_html/aboutus.html')

def getcontactus(request):
    return render(request,'suchana_html/contactus.html')
