from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

#from django.core.exception import PermissionDenied
#import six
#from django.contrib.auth.decorators import user_passes_test


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func



#to prevent users from accessing certain pages

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group=None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            
            else:
                messages.info(request, 'you cant view that page')
                return redirect('register')
                
        return wrapper_func
    return decorator









#to limit the from certain pages

# def allowed_users(allowed_roles=[]):
#     def decorator(view_func):
#         def wrapper_func(request, *args, **kwargs):

#             group = None
#             if request.user.groups.exists():
#                 group = request.user.groups.all()[0].name
            
#             if group in allowed_roles:
#                 return view_func(request, *args, **kwargs)
#             else:
#                 return HttpResponse('Your are not authorized to view this page')
#         return wrapper_func
#     return decorator
            

# def group_required(group, login_url=None, raise_exception=False):
#     def check_perms(user):
#         if isinstance(group, six.string_types):
#             groups= (group, )
#         else:
#             groups = group

#         if user.group.filter(name__in=groups).exists():
#             return True
#         if raise_exception:
#             raise PermissionDenied
#         return False