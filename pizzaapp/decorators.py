from django.shortcuts import render, redirect
from django.http import HttpResponse


def admin_login_required(function):
    def wrap(request,*args,**kwargs):
        # print(request.session.get('user'))
        if request.session.get('user'):
            return function(request,*args,**kwargs)
        else:
            return redirect('/admin/')
    return wrap

def user_login_required(function):
    def wrap(request,*args,**kwargs):
        print(request.session.get('user'))
        if request.session.get('user'):
            return function(request,*args,**kwargs)
        else:
            return redirect('/loginuser/')
    return wrap
