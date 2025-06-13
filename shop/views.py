from django.shortcuts import render,redirect
from django.http import JsonResponse
from .forms import *
from api.models import Login
from api.serializers import *
# Create your views here.
def home(request):
    if request.method=='POST':
        uname=request.POST['username']
        pword=request.POST['password']
        user_instance=Login.objects.filter(username=uname,password=pword,usertype="shop")
        if user_instance:
            return redirect(homepage)
        else:
            return render(request,'home.html')
    return render(request,'home.html')



def homepage(request):
    
    return render(request,"homepage.html")

def upload_items(request):
    frm=additemform()
    if request.method=="POST":
        frm=additemform(request.POST,request.FILES)
        if frm.is_valid():
            frm.save()
        else:
            pass

    return render(request,'additem.html',{'frm':frm})


def delete_items(request):
    item_data=items.objects.all()
    
        
   
    return render(request,"delete_item.html",{"items":item_data})


def delete(request,item_id):
     items.objects.filter(id=item_id).delete()
     return redirect("delete_items")


def manage_orders(request):
   
    approved=Orders.objects.filter(status="ordered")
    delivered=Orders.objects.filter(status="delivered")
    if request.POST:
        choice=request.POST["choice"]
        order_id=request.POST["order_id"]
        Orders.objects.filter(id=order_id).update(status=choice)

    return render(request,"manage_orders.html",{'approved':approved,'delivered':delivered})
    



    