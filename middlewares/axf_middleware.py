

from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from axf.models import User

LOGIN_REQUIRED_JSON=["/addtocart/","/subtocart/",'/makeorders/','/pay/']
LOGIN_REQUIRED=['/orderdetail/','ordernodetail/','/gocart/','/mine/']

class LoginMiddleware(MiddlewareMixin):
    def process_request(self,request):
        if request.path in LOGIN_REQUIRED_JSON:
            user_id=request.session.get('user_id')
            if user_id:
                user=User.objects.get(pk=user_id)
                request.user=user
            else:
                return JsonResponse({'status':'900'})
        if request.path in LOGIN_REQUIRED:
            user_id=request.session.get('user_id')
            if user_id:
                user=User.objects.get(pk=user_id)
                request.user=user
            else:
                return redirect(reverse('axf:login'))