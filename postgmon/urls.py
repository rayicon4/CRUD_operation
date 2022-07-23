from django.urls import path
from .views import home, update, delete, loginpage, register, logoutuser, userpage


urlpatterns = [
    path('', loginpage, name='loginpage'),
    path('logoutuser/', logoutuser, name='logoutuser'),
    path('user/', userpage, name='userpage'),
    path('home/', home, name='home'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('register/', register, name='register'),
]