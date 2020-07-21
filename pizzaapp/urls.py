from .views import adminlogin,authenticateadmin,adminhomepageview,adminlogoutview,adminforgetpasswordview,addpizzaview,deletepizzaview,updatepizzaview,homepageview,signupuserview,loginuserview,authenticateuser,welcomeuserview,userlogoutview,placeorderview,userordersview,adminordersview,acceptorderview,declineorderview
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', adminlogin,name = 'adminloginpage'),
    path('authenticateadmin/',authenticateadmin),
    path('admin/homepage/',adminhomepageview, name = 'adminhomepage'),
    path('adminlogout/',adminlogoutview),
    path('adminforgetpassword/',adminforgetpasswordview, name = 'adminforgetpassword'),
    path('addpizza/',addpizzaview),
    path('deletepizza/<int:id>/',deletepizzaview),
    path('updatepizza/<int:id>/',updatepizzaview),
    path('',homepageview,name = 'homepage'),
    path('signupuser/',signupuserview),
    path('loginuser/',loginuserview, name = 'loginuserpage'),
    path('user/authenticateuser/',authenticateuser),
    path('user/welcomeuser/',welcomeuserview, name = 'userwelcomepage'),
    path('userlogout/',userlogoutview),
    path('placeorder/',placeorderview),
    path('userorders/',userordersview),
    path('adminorders/',adminordersview),
    path('acceptorder/<int:orderpk>/',acceptorderview),
    path('declineorder/<int:orderpk>/',declineorderview),
]
