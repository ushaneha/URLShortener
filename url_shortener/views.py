from django.shortcuts import render,redirect
from django.http import HttpResponse # import HttpResponse to implement http response functionalities
from .models import LongtoShort
# Create your views here.
def helloworld(request):
    return HttpResponse('Hello : I am great and I am learning Django') #function for http://127.0.0.1:8000/hello

def home_page(request):
    context={"error": False,"submitted":False}
    if request.method=="POST":
        data=request.POST
        longurl=data['longurl']
        customname=data['custom_name']
        
        
        try:
            obj=LongtoShort(long_url=longurl,custom_name=customname)
            obj.save()
            context["submitted"]=True
            context["long_url"]=longurl
            context["custom_name"]=customname
            context["date"]=obj.created_date
            context["visited"]=obj.visit_count
        except:
            context['error']=True

    return render(request,"index.html",context)






def redirect_url(request,customname):
    row=LongtoShort.objects.filter(custom_name=customname)
    if len(row)==0:
        return HttpResponse("This endpoint doesn't exist. ERROR!!")
    obj=row[0]
    long_url=obj.long_url
    obj.visit_count+=1
    obj.save()
    print(long_url)
    return redirect(long_url)




def all_analytics(request):
    rows=LongtoShort.objects.all()
    context={
        "rows":rows
    }
    return render(request,"analytics.html",context)