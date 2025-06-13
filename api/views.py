from django.shortcuts import render
from .models import *
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from shop.models import items
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@csrf_exempt
@api_view(["POST"])
def registration(request):
     if request.method=='POST':
          fname=request.POST['fname']
          email=request.POST['email']
          uname=request.POST['uname']
          pword=request.POST['pword']
          login_instance=Login.objects.create(username=uname,password= pword)
          if login_instance:
               u= User.objects.create(firstname=fname,email=email,login=login_instance)
               serializer=UserSerializer(u)
               return Response({'status':'success','user_data':serializer.data})
          

@csrf_exempt
@api_view(["GET"])
def login(request):
     if request.method=="GET":
          uname=request.GET['uname']
          pword=request.GET['pword']   
          login_instance=Login.objects.get(username=uname,password=pword)
          user_instance=User.objects.get(login=login_instance)
          serializer=UserSerializer(user_instance)

          return Response({'status':'success','username':login_instance.username,'user_data':serializer.data})
          

@csrf_exempt
def update(request):
     if request.method=="POST":
          uname=request.POST['uname']
          fname=request.POST['fname']
          user_id=request.POST['user_id']
          user_instance=User.objects.get(id=user_id)
          user_instance.firstname=fname
          user_instance.save()
          login_instance=user_instance.login
          login_instance.username=uname
          login_instance.save()
          return JsonResponse({'status':'success'})
         

@csrf_exempt   
@api_view(["GET"])      
def getitems(request):

     if request.method=="GET":
          itemss=items.objects.all()
          serializer=ItemsSerializer(itemss,many=True)
          return Response({'status':"success",'items_data':serializer.data})


          
@csrf_exempt
def addtocart(request):
     if request.POST:
          item_id=request.POST["item_id"]
          user_id=request.POST["user_id"]
          item_instance=items.objects.get(id=item_id)
          user_instance=User.objects.get(id=user_id)
          if item_instance:
               cart_instance=Cart.objects.create(user=user_instance,item=item_instance,status="cart")
               
               return JsonResponse({"status":"success"})

@csrf_exempt
def cartdetails(request):
     user_id=request.GET['user_id']
     if user_id:
          # user_instance is your User object
          user_instance=User.objects.get(id=user_id)
         

          # Get all Cart objects for this user
          cart_instance= Cart.objects.filter(user=user_instance)

        
          
          # OR more efficiently, using `.values_list()` to get item ids
          item_ids = cart_instance.values_list('item', flat=True)

          # If you want full item objects, query items with those ids
          items_for_user = items.objects.filter(id__in=item_ids).values()
         
          items_list=list(items_for_user)
          

          
          return JsonResponse({'status':"success",'items_list':items_list})
     

@csrf_exempt
def addtoorders(request):
     item_id=request.POST["item_id"]
     user_id=request.POST["user_id"]
     user_instance=User.objects.get(id=user_id)
     item_instance=items.objects.get(id=item_id)
     ordered= Orders.objects.create(item=item_instance,user=user_instance,status="ordered")
    
     if ordered:
        Cart.objects.filter(user=user_instance,item=item_instance).delete()
     
     
     return JsonResponse({'status':"success"})


@csrf_exempt
def getOrdereditems(request):
     user_id=request.GET["user_id"]
     user_instance=User.objects.get(id=user_id)
     orders=Orders.objects.filter(user=user_instance).exclude(status="delivered")
     item_ids=orders.values_list('item',flat=True)
     order_items=items.objects.filter(id__in=item_ids).values()
     order_list=list(order_items)
     return JsonResponse({"status":"success","item_list":order_list})


@csrf_exempt
@api_view(["GET"])
def retrieveorderprogress(request):
     user_id=request.GET["user_id"]
     user_instance=User.objects.get(id=user_id)
     order_instance=Orders.objects.filter(user=user_instance,status="approve")
     item_ids=order_instance.values_list("item",flat=True)
     itemss=items.objects.filter(id__in=item_ids)
     serializer=ItemsSerializer(itemss,many=True)
     print(serializer)
     return Response({"status":"success","item_list":serializer.data})