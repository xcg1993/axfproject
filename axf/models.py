from django.db import models
#insert into axf_wheel(img,name,trackid) values("http://img01.bqstatic.com//upload/activity/2017031716035274.jpg@90Q.jpg","酸奶女王","21870"),("http://img01.bqstatic.com//upload/activity/2017031710450787.jpg@90Q.jpg","优选圣女果","21869"),("http://img01.bqstatic.com//upload/activity/2017030714522982.jpg@90Q.jpg","伊利酸奶大放价","21862"),("http://img01.bqstatic.com//upload/activity/2017032116081698.jpg@90Q.jpg","鲜货直供－窝夫小子","21770"),("http://img01.bqstatic.com//upload/activity/2017032117283348.jpg@90Q.jpg","鲜货直供－狼博森食品","21874");
from axf.constants import ORDER_STATE_NO_PAY, ACCEPT_NO_JUDGEMENT, NOACCEPT_NO_JUDGEMENT


class Wheel(models.Model):
     img=models.CharField(max_length=200)
     name = models.CharField(max_length=200)
     trackid=models.CharField(max_length=30)
#insert into axf_nav(img,name,trackid) values("http://img01.bqstatic.com//upload/activity/2017032016495169.png","每日必抢","21851"),("http://img01.bqstatic.com//upload/activity/2016121920130294.png","每日签到","21753"),("http://img01.bqstatic.com//upload/activity/2017010517013925.png","鲜货直供","21749"),("http://img01.bqstatic.com//upload/activity/2017031518404137.png","鲜蜂力荐","21854");

class Nav(models.Model):#导航模型
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    trackid = models.CharField(max_length=30)

#insert into axf_mustbuy(img,name,trackid) values("http://img01.bqstatic.com//upload/activity/2017031715194326.jpg@90Q.jpg","酸奶女王","21870"),("http://img01.bqstatic.com//upload/activity/cms_118826_1489742316.jpg@90Q","鲜果女王","21861"),("http://img01.bqstatic.com//upload/activity/2017031011044918.jpg@90Q.jpg","麻辣女王","21866"),("http://img01.bqstatic.com//upload/activity/2017022318314545.jpg@90Q.jpg","鲜货直供－果析","21858");
class Mustbuy(models.Model):        #必购模型
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    trackid = models.CharField(max_length=30)

#insert into axf_shop(img,name,trackid) values("http://img01.bqstatic.com//upload/activity/2016121616565087.png@90Q.png","闪送超市","1464"),("http://img01.bqstatic.com//upload/activity/2017031018405396.png@90Q.png","热销榜","104749"),("http://img01.bqstatic.com//upload/activity/2017031018403438.png@90Q.png","新品尝鲜","104747"),("http://img01.bqstatic.com//upload/activity/2016121618424334.png@90Q.png","牛奶面包","103536"),("http://img01.bqstatic.com//upload/activity/2016121617150246.png@90Q.png","饮料酒水","103549"),("http://img01.bqstatic.com//upload/activity/201612161714501.png@90Q.png","优选水果","103532"),("http://img01.bqstatic.com//upload/activity/2016121618550639.png@90Q.png","更多","100001"),("http://img01.bqstatic.com//upload/activity/2017031318520359.jpg@90Q.jpg","鲜蜂力荐","21854"),("http://img01.bqstatic.com//upload/activity/2016121618233839.png@90Q.png","卤味-鸭货不能停","21742"),("http://img01.bqstatic.com//upload/activity/2016121618232773.png@90Q.png","零食轰趴","21142"),("http://img01.bqstatic.com//upload/activity/2016121618235123.png@90Q.png","整箱购","20581");
class Shop(models.Model):      #店铺模型
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    trackid = models.CharField(max_length=30)


class Mainshow(models.Model):
    trackid = models.CharField(max_length=30)
    name = models.CharField(max_length=200)
    img = models.CharField(max_length=200)
    categoryid=models.CharField(max_length=30)
    brandname=models.CharField(max_length=30)
    img1=models.CharField(max_length=200)
    childcid1=models.CharField(max_length=30)
    productid1=models.CharField(max_length=30)
    longname1=models.CharField(max_length=50)
    price1=models.FloatField()
    marketprice1=models.FloatField()
    img2 = models.CharField(max_length=200)
    childcid2=models.CharField(max_length=30)
    productid2=models.CharField(max_length=30)
    longname2=models.CharField(max_length=50)
    price2=models.FloatField()
    marketprice2=models.FloatField()
    img3 = models.CharField(max_length=200)
    childcid3=models.CharField(max_length=30)
    productid3=models.CharField(max_length=30)
    longname3=models.CharField(max_length=50)
    price3=models.FloatField()
    marketprice3=models.FloatField()


class Foodtypes(models.Model):
    typeid=models.CharField(max_length=20)
    typename=models.CharField(max_length=20)
    childtypenames=models.CharField(max_length=200)
    typesort=models.IntegerField()


class Goods(models.Model):
    productid=models.CharField(max_length=20)
    productimg=models.CharField(max_length=150)
    productname=models.CharField(max_length=100)
    productlongname=models.CharField(max_length=200)
    isxf=models.BooleanField()
    pmdesc=models.BooleanField()
    specifics=models.CharField(max_length=20)
    price=models.FloatField()
    marketprice=models.FloatField()
    categoryid=models.IntegerField()    #大类别的标识
    childcid=models.IntegerField()      #小类别的标识
    childcidname=models.CharField(max_length=30)
    dealerid=models.CharField(max_length=20)
    storenums=models.IntegerField()
    productnum=models.IntegerField()


class User(models.Model):
    username=models.CharField(max_length=12,unique=True)
    password=models.CharField(max_length=256)
    tel=models.CharField(max_length=15)
    address=models.CharField(max_length=30)
    icon=models.ImageField(upload_to='icons/%Y/%m/%d')


class Cart(models.Model):
    goods=models.ForeignKey(Goods,on_delete=models.CASCADE)         #关联商品
    user=models.ForeignKey(User,on_delete=models.CASCADE)       #关联用户
    cart_num=models.IntegerField()      #购物车中商品的数量
    ischoose=models.BooleanField(default=1) #购物车选中状态

class Orders(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)#订单关联用户
    totalPrice=models.FloatField()
    ordertime=models.DateTimeField(auto_now=True)
    orderstate=models.IntegerField(default=ORDER_STATE_NO_PAY)
    jugementstate=models.IntegerField(default=NOACCEPT_NO_JUDGEMENT)

class OrderGoods(models.Model):#放入订单中的商品
    orders=models.ForeignKey(Orders,on_delete=models.CASCADE)
    goods=models.ForeignKey(Goods,on_delete=models.CASCADE)
    goods_num=models.IntegerField()