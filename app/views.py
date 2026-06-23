from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
from django.db.models import Q

# Create your views here.

def insert_topic(request):
    Topic_name = input('Enter Topic_name:')
    LTO = Topic.objects.filter(Topic_name=Topic_name)

    if LTO:
        return HttpResponse('Topic already exists in DB')
    else:
        Topic.objects.get_or_create(Topic_name=Topic_name)
        return HttpResponse('Topic inserted successfully')
        
    
def insert_webpage(request):
    for TO in Topic.objects.all():
        print(TO.Topic_name)

    Topic_name = input('enter TopicName:')
    LTO=Topic.objects.filter(Topic_name=Topic_name)

    if LTO:
        TO = LTO[0]
        Name=input('Enter Name:')
        Url = input('Enter URl:')
        Email = input('Enter Email:')
        TWO = Webpage.objects.get_or_create(Topic_name=TO,Name=Name,Url=Url,Email=Email)
        if TWO[1]:
            return HttpResponse('New webpage is Created')
        else:
            return HttpResponse('Webpage is present in DB')
    else:
        return HttpResponse(f'{Topic_name} is not present Table OB')

def insert_AccessRecord(request):
    Name=input('Enter Name:')
    LWO = Webpage.objects.filter(Name=Name)
    if LWO:
        WO = LWO[0]
        Author = input('Enter Author:')
        Date = input('Enter Date:')
        TWO=AccessRecord.objects.get_or_create(Name=WO,Author=Author,Date=Date)
        if TWO[1]:
            return HttpResponse('Data inserted Sucessfully')
        else:
            return HttpResponse('Data is already present')
    else:
        return HttpResponse('Name is not there')
    



def display_Topic(request):
    QLTO = Topic.objects.all()
    d = {'QLTO':QLTO}

    return render(request,'display_topic.html',d)

def display_webpage(request):
    QLWO = Webpage.objects.all()

    QLWO=Webpage.objects.filter(Topic_name='Cricket')
    QLWO=Webpage.objects.exclude(Topic_name='Cricket')
    QLWO=Webpage.objects.all()[4:7]
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.all().order_by('Name')
    QLWO=Webpage.objects.all().order_by('-Name')
    QLWO=Webpage.objects.all().order_by(Length('Name'))
    QLWO=Webpage.objects.all().order_by(Length('Name').desc())
    QLWO=Webpage.objects.filter(pk__in=(1,6))
    QLWO=Webpage.objects.filter(pk__range=(1,6))
    QLWO=Webpage.objects.filter(pk__isnull=True)
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(Name__startswith='a')
    QLWO=Webpage.objects.filter(Name__endswith='a')
    QLWO=Webpage.objects.filter(Name__contains='a')
    QLWO=Webpage.objects.filter(Name__regex='^A\w+')
    QLWO=Webpage.objects.filter(pk__lte=3) #showing 1to 3
    QLWO=Webpage.objects.filter(pk__lt=3)  # showing only 1,2
    QLWO=Webpage.objects.filter(pk__gt=3) # Greater then 3 means 4,5,6,7
    QLWO=Webpage.objects.filter(pk__gte=3) # Also 3 and greater then 3 means 3,4,5,6,7

    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(Topic_name='Cricket',Url__endswith='in')
    QLWO=Webpage.objects.filter(Q(Topic_name='Online Game')|Q(Url__endswith='in')& Q(Name__startswith='a'))



    d = {'QLWO':QLWO}
    return render(request,'display_webpage.html',d)

def display_accessrecord(request):
    QLAO=AccessRecord.objects.all()
    QLAO = AccessRecord.objects.filter(Date__month=10)
    QLAO = AccessRecord.objects.filter(Date__year=2025)
    QLAO = AccessRecord.objects.filter(Date__day=28)
    



    d = {'QLAO':QLAO}
    return render(request,'display_accessrecord.html',d)
    


    


    
        

