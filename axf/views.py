import hashlib
import time

from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.urls import reverse

from axf.constants import ORDER_STATE_PAIED, ACCEPT_NO_JUDGEMENT
from axf.models import *
from axf.view_helper import total_price


def home(request):
    wheelsList=Wheel.objects.all()
    navList=Nav.objects.all()
    mustbuyList=Mustbuy.objects.all()
    shops=Shop.objects.all()
    shop1=shops[0]
    shop2= shops[1:3]
    shop3 = shops[3:7]
    shop4 = shops[7:11]
    mainList=Mainshow.objects.all()
    return render(request,'axf/home.html',locals())



def market(request,foodtypeid,childtypeid,sortcode):
    leftSlider=Foodtypes.objects.all()
    if childtypeid=='0':
        productList=Goods.objects.filter(categoryid=foodtypeid)
    else:
        productList=Goods.objects.filter(categoryid=foodtypeid,childcid=childtypeid)
    child_dict={}
    food=Foodtypes.objects.get(typeid=foodtypeid)
    childnames=food.childtypenames
    childlist=childnames.split('#')
    for child in childlist:
        temp=child.split(':')
        child_dict[temp[0]]=temp[1]

    if sortcode=='1':
        productList=productList.order_by('productnum')
    elif sortcode=='2':
        productList=productList.order_by('price')
    elif sortcode=='3':
        productList=productList.order_by('-price')

    user_id=request.session.get('user_id')
    if user_id:
        for product in productList:
            carts=Cart.objects.filter(user_id=user_id,goods_id=product.id)
            if carts.exists():
                cart=carts.first()
                product.cart_num=cart.cart_num
            else:
                product.cart_num=0
    return render(request,'axf/market.html',locals())



#进入购物车
def gocart(request):
    carts=Cart.objects.filter(user=request.user)
    if carts.exists():
        select_all_flag=not Cart.objects.filter(user=request.user,ischoose=False).exists()
    else:
         select_all_flag=False
    totalPrice=total_price(request)
    return render(request,'axf/cart.html',locals())


def addShopping(request):
    print('进入了addshopping函数')
    goods_id=request.GET.get('goods_id')#接受ajax传过来的goods_id
    data={
        'status':'200',
    }
    carts=Cart.objects.filter(goods_id=goods_id,user=request.user)
    if carts.exists():
        cart=carts.first()
        cart.cart_num+=1
        cart.save()   #更新购物车
    else:
        cart=Cart.objects.create(goods_id=goods_id,user=request.user,cart_num=1)
    totalPrice = total_price(request)
    data['totalPrice'] = totalPrice
    data['cart_num']=cart.cart_num
    return JsonResponse(data)


#从购物车中减
def subShopping(request):
    print('进入了subshopping函数')
    goods_id=request.GET.get('goods_id')#接受ajax传过来的goods_id
    data = {
        'status': '200',
    }
    carts=Cart.objects.filter(goods_id=goods_id,user=request.user)
    if carts.exists():
        cart=carts.first()
        cart.cart_num-=1
        if cart.cart_num==0:
            data['cart_num']=0
            cart.delete()
        else:
            cart.save()
        data['cart_num']=cart.cart_num
        totalPrice=total_price(request)
        data['totalPrice']=totalPrice
    else:
        data['status']='901'
        data['msg']='从未添加该商品到购物车中'

    return JsonResponse(data)







def mine(request):
    # user_id = request.session.get("user_id")  # 从session中取出user_id
    # if user_id:
    #     user = User.objects.get(id=user_id)
    username = request.user.username
    figure_path = "uploads/" + request.user.icon.name
    order_nopay_count=Orders.objects.filter(user_id=request.user.id,orderstate=ORDER_STATE_NO_PAY).count()
    order_pay_count = Orders.objects.filter(user_id=request.user.id, orderstate=ORDER_STATE_PAIED).count()
    accept_no_judgement=Orders.objects.filter(user_id=request.user.id, jugementstate=ACCEPT_NO_JUDGEMENT).count()
    # else:
    #     username = "登录"
    return render(request,'axf/mine.html',locals())


def register(request):
    if request.method == "GET":
        return render(request,'axf/register.html')
    elif request.method == "POST":
        userAccount = request.POST.get("userAccount")  # 接收提交的POST数据
        userPass = request.POST.get("userPass")
        userPhone = request.POST.get("userPhone")
        userAddress = request.POST.get("userAddress")
        userImg = request.FILES.get("userImg")  # 接收二进制图片
        print("userImg.name=",userImg.name)
        userImg.name = str(int(time.time()*10000)) + userImg.name  # 重新设定图片名称
        new_user = User()
        new_user.username = userAccount
        md5 = hashlib.md5()
        md5.update(userPass.encode("utf-8"))
        new_user.password = md5.hexdigest()
        new_user.tel = userPhone
        new_user.address = userAddress
        new_user.icon = userImg  # 将图片对象与用户对象关联
        new_user.save()
        return redirect(reverse("axf:login"))


def login(request):   # 登录
    if request.method == "GET":
        return render(request,'axf/login.html')
    elif request.method == "POST":
        loginname = request.POST.get("loginname")
        loginpwd = request.POST.get("loginpwd")
        md5 = hashlib.md5()
        md5.update(loginpwd.encode("utf-8"))
        loginpwd = md5.hexdigest()
        users = User.objects.filter(username=loginname,password=loginpwd)
        if users:
            user = users.first()
            request.session["user_id"] = user.id  # 登录成功后，设置session属性

            return redirect(reverse("axf:mine"))
        else:
            return redirect(reverse("axf:login"))


def logout(request):
    request.session.flush()
    return redirect(reverse("axf:mine"))


def change_cart_select(request):
    cartid=request.GET.get('cartid')
    cart=Cart.objects.get(pk=cartid)
    cart.ischoose=not cart.ischoose  #取反
    cart.save()
    totalPrice=total_price(request) #总价
    print(totalPrice)

    user_id=request.session.get('user_id')
    select_all_flag= not Cart.objects.filter(user_id=user_id,ischoose=False).exists()
    data={
        'ischoose':cart.ischoose,
        'select_all_flag':select_all_flag,
        'totalPrice':totalPrice,
    }
    return JsonResponse(data)



def change_select_all(request):#改变全选状态
    is_select=request.GET.get('hope_status')
    print(is_select)
    user_id=request.session.get('user_id')
    carts=Cart.objects.filter(user_id=user_id)
    if is_select=='true':
        for cart in carts:
            cart.ischoose=True
            cart.save()
    else:
        for cart in carts:
            cart.ischoose=False
            cart.save()
    totalPrice=total_price(request)
    data={
        'is_select':is_select,
        'totalPrice':totalPrice,
    }
    return JsonResponse(data)




def make_order(request):
    allcarts=Cart.objects.all()
    if allcarts.exists():
        carts=Cart.objects.filter(user=request.user,ischoose=True)
        orders=Orders()
        orders.user=request.user
        orders.totalPrice=total_price(request)
        orders.save()
        for cart in carts:
            order_goods=OrderGoods()#创建订单商品对象
            order_goods.orders=orders#关联订单对象
            order_goods.goods=cart.goods
            order_goods.goods_num=cart.cart_num
            order_goods.save()
            cart.delete()
        data={
            'orderid':orders.id,
            'status':'200',
        }
    else:
        print('没有商品')
        data={
            'status':'902'
        }
    return JsonResponse(data)

def order_no_detail(request):
    # order_id=request.GET.get('order_id')
    order=Orders.objects.filter(orderstate=ORDER_STATE_NO_PAY)
    #,orderstate=ORDER_STATE_NO_PAY
    return render(request,'axf/order_detail.html',locals())

def order_detail(request):
    order_id=request.GET.get('order_id')
    order=Orders.objects.filter(id=order_id)
    return render(request,'axf/order_detail.html',locals())

def pay(request):
    order_id=request.GET.get('order_id')
    order=Orders.objects.get(pk=order_id)
    order.orderstate=ORDER_STATE_PAIED
    order.jugementstate=ACCEPT_NO_JUDGEMENT
    order.save()
    data={
        'status':'200',
        'msg':'支付成功',
    }
    return JsonResponse(data)




