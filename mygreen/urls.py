from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns =[
        path('',views.home,name='home'),
        path('registration/',views.Registration,name='registration'),
        path('login/',views.Login,name='login'),
        path('services/',views.services,name='services'),
        path('shop/',views.shop,name='shop'),
        path('logout/',views.Logout,name='logout'),
        path('productview/<str:pk>/',views.productview,name='productview'),
        path('addcart/<str:pk>/',views.addcart,name='addcart'),
        path('cart/',views.cart,name='cart'),
        path('cartremove/<str:pk>',views.cartremove,name='cartremove'),
        path('buy/<str:pk>/',views.buy,name='buy'),
        path('orderhistory/',views.orderhistor,name='orderhistory'),
        path('customerprofile/',views.customerprofile,name='customerprofile'),
        path('editprofile/',views.editprofile,name='editprofile'),
        path('orderdetails/<str:pk>/',views.orderdetails,name='orderdetails'),
        path('orderdelete/<str:pk>/',views.orderdelete,name='orderdelete'),
        path('adminorderhistory/',views.adminorderhistory,name='adminorderhistory'),
        path('adminorderupdate/<str:pk>/',views.adminorderupdate,name='adminorderupdate'),

        path('resetpassword/',auth_view.PasswordResetView.as_view(template_name='mygreen/resetpassword.html'),
                name='password_reset'),
        path('resetpasswordsend/',auth_view.PasswordResetDoneView.as_view(template_name='mygreen/resetpasswordsend.html'),
                name='password_reset_done'),
        path('reset/<uidb64>/<token>',auth_view.PasswordResetConfirmView.as_view(template_name='mygreen/resetpasswordform.html'),
                name='password_reset_confirm'),
        path('resetpasswordcomplete/',auth_view.PasswordResetCompleteView.as_view(template_name='mygreen/resetpasswordcomplete.html'),
                name='password_reset_complete')

]