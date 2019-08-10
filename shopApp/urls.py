from django.urls import path
from .views import shopAppView,itemDetail,productsView



urlpatterns = [
    path('',shopAppView.as_view(),name='home'),
    path('itemdetail/',itemDetail,name='detail'),
    path('products/',productsView),

]
