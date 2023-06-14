
from django.urls import path
from . import views

urlpatterns = [
    # path('login/', views.loginPage, name="login"),
    # path('logout/', views.logoutUser, name="logout"),
    # path('register/', views.registerPage, name="register"),
    path('activos/', views.activos, name='activos'),
    path('detalle-accion/<str:symbol>/', views.detalle_accion, name='detalle_accion'),

    path('', views.space, name="home"),
    path('create-space/',  views.createSpace, name='create-space'),
    path('update-space/<str:pk>/',  views.updateSpace, name='update-space'),
    path('delete-space/<str:pk>/',  views.deleteSpace, name='delete-space'),
    path('space/<str:pk>/', views.space, name="space"),
    path('trading/', views.trading, name="trading"),

]





