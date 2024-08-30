from django.urls import path
from .views import UserViewSet, MenuItemView, SingleMenuItemView, BookingViewSet, MenuItemListCreateView, MenuItemDetailUpdateView, msg

urlpatterns = [
    path('users/', UserViewSet.as_view({'get': 'list'})),
    path('menu/', MenuItemView.as_view()),
    path('menu/<int:pk>/', SingleMenuItemView.as_view()),
    path('menu-items/', MenuItemListCreateView.as_view()),
    path('menu-items/<int:pk>/', MenuItemDetailUpdateView.as_view()),
    path('booking/', BookingViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('booking/<int:pk>/', BookingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('message/', msg),
]
