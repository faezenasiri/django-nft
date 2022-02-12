

from django.urls import path, include
from .views import nftViewSet , nftdetail , userpview ,userpviewdetail, userpviewdetailpk  
from .views import nftdetail






urlpatterns = [
    path('nft/', nftViewSet.as_view()),
    path('nft/<int:pk>/', nftdetail.as_view()),
    path('userp/', userpview.as_view()),
    path('userp/<int:pk>', userpviewdetail.as_view()),
    path('userpk/<str:public_key>', userpviewdetail.as_view()),


]


