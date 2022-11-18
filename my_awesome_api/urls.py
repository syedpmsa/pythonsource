from django.urls import include, path

from rest_framework import routers
from . import views

from my_awesome_api.views import AccountViewSet, DestinationViewSet

router = routers.DefaultRouter()
router.register(r'people', AccountViewSet)
router.register(r'Destination', DestinationViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('Add_account/',views.add_Account, name='Add-account'),
   path('add_destination/',views.add_Destination, name='add-Destination'),
   path('view_account/', views.view_Account, name='view_account'),
   path('view_destination/', views.view_Destination, name='view_destination'),
   path('update_account/<int:pk>/', views.update_Account, name='update-Account'),
   path('update_destination/<int:pk>/', views.update_Destination, name='update-destination'),
   path('delete_account/delete/<int:pk>', views.delete_Account, name='delete-Account'),
   path('delete_destination/delete/<int:pk>', views.delete_Destination, name='delete-destination'),
   path('urls_destination/<int:pk>', views.url_destionation, name='account_detail')
   
]