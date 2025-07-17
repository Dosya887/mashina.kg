from django.urls import path
from . import views
urlpatterns = [
    path('', views.show_display, name='show_display'),
    path('car_info/<int:car_id>/', views.car_info, name='car_info'),
]
