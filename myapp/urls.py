from django.urls import path
from . import views 

urlpatterns = [
   path('', views.profile, name='home'),
   path('index/', views.dashboard, name='index'),
   path('holiday/', views.holiday_page, name='holiday'),
   path('login/', views.logout_page, name='login'),
   path('forgot/',views.forget_password, name='forgot'),
   path('update-user-info/', views.update_user_info, name='update-user-info'),
    
]



