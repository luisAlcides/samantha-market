
from django.urls import path
from . import views

urlpatterns = [
    # path('login/', views.loginPage, name="login"),
    # path('logout/', views.logoutUser, name="logout"),
    # path('register/', views.registerPage, name="register"),
    path('activos/', views.activos, name='activos'),
    path('detalle-accion/<str:symbol>/', views.detalle_accion, name='detalle_accion'),

    path('', views.activos, name="home"),

    path('blog/', views.blog, name="blog"),
    path('trading/', views.trading, name="trading"),

]





