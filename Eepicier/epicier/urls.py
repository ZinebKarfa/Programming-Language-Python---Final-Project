from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home , name="home"),
    path('produits/',views.produits,name="produits"),
    path('produits/create',views.produitCreate,name="produitCreate"),
    path('produits/update/<str:pk>',views.produitupdate,name="produitupdate"),
    path('produits/delete/<str:pk>',views.produitdelete,name="produitdelete"),
    path('clients/',views.clients,name="clients"),
    path('clients/create',views.clientCreate,name="clientCreate"),
    path('clients/update/<str:pk>',views.clientupdate,name="clientupdate"),
    path('clients/delete/<str:pk>',views.clientdelete,name="clientdelete"),
    path('clients/<str:pk>',views.client ,name="client"),
    path('clients/<str:pk>/unpaid',views.clientunpaid ,name="clientunpaid"),
    path('clients/<str:pk>/paid',views.clientpaid ,name="clientpaid"),
    path('credits/',views.credits,name="credits"),
    path('credits/unpaid',views.creditunpaid,name="creditunpaid"),
    path('credits/paid',views.creditpaid,name="creditpaid"),
    path('credits/create',views.creditCreate,name="creditCreate"),
    path('credits/update/<str:pk>',views.creditupdate,name="creditupdate"),
    path('credits/updatestatus/<str:pk>',views.creditupdatestatus,name="creditupdatestatus"),
    path('credits/delete/<str:pk>',views.creditdelete,name="creditdelete"),

    path('login/',views.userLogin,name="login"),
    path('logout/',views.userlogout,name="logout"),
    path('register/',views.register,name="register"),

]