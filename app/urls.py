from django.urls import path
from . import views
urlpatterns = [
    path('', views.show_display, name='show_display'),
    path('car_info/<int:car_id>/', views.car_info, name='car_info'),
    path('add/', views.add_car, name='add_car'),
    path('delete/<int:car_id>/', views.delete_car, name='delete_car'),
    path('update/<int:car_id>/', views.update_car, name='update_car'),
    path('user_register/', views.user_register, name='register'),
    path('user_login/', views.user_login, name='login'),
    path('user_logout/', views.user_logout, name='logout'),
]
