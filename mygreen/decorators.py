from django.shortcuts import redirect
from django.http import HttpResponse

def restrict_login(view_fun):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('shop')
        else:
            return view_fun(request,*args,**kwargs)
    return wrapper

def allow_user(allow_role=[]):
    def decorate_fun(view_fun):
        def wrapper_fun(request,*args,**kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allow_role:
                return view_fun(request,*args,**kwargs)
            else:
                return HttpResponse("your not allowed to this page")
        return wrapper_fun
    return decorate_fun