from django.contrib import admin
from rest_framework import routers
from Restaurant import views
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


# Configuración del router
router = routers.DefaultRouter() # Creación del router
router.register(r'users', views.UserViewSet) # Registro de la vista UserViewSet
router.register(r'booking', views.BookingViewSet)  # Registro de la vista BookingViewSet
router.register(r'menu', views.MenuViewSet)  # Registro de la vista MenuViewSet
router.register(r'menu-item', views.MenuItemViewSet)  # Registro de la vista MenuItemViewSet

urlpatterns = [
    path('admin/', admin.site.urls), # URL de administrador
    path('', include(router.urls)),  # Rutas del router principal
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # Autenticación de la API
    path('api-token-auth/', obtain_auth_token), # URL para obtener el token de autenticación
    path('api/', include('Restaurant.urls')),  # Incluye las URLs de la app Restaurant
    path('auth/', include('djoser.urls')), # Incluye las URLs de la app djoser
    path('auth/', include('djoser.urls.authtoken')) # Incluye las URLs de la app djoser para el token de autenticación

]
