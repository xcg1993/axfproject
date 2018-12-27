from django.conf.urls import url
from django.urls import path

from axf.views import *


app_name='axf'
urlpatterns = [
    url(r'^home/$',home,name='home'),
    path('market/<foodtypeid>/<childtypeid>/<sortcode>/',market,name='market'),
    path('mine/',mine,name='mine'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('gocart/',gocart,name='gocart'),
    path('addtocart/',addShopping),
    path('subtocart/',subShopping),
    path('changeselect/',change_cart_select),
    path('changeselectall/',change_select_all),
    path('makeorders/',make_order),
    path('orderdetail/',order_detail),
    path('pay/',pay),
    path('ordernodetail/',order_no_detail,name='ordernodetail')
]