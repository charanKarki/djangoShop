from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from .views import signup

urlpatterns = [
    path('login/',LoginView.as_view(template_name = 'login.html',
                                                        extra_context=  {
                                                            'next':'/'
                                                            })
                                                            ,name= 'login'),
                                                            
    path('logout/',LogoutView.as_view(next_page='/'),name = 'logout'),
    path('signup/',signup.as_view(),name = 'signup')
]
