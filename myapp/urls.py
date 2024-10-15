from django.urls import path
from . import views 





urlpatterns = [
   path('', views.profile, name='home'),
   path('index/', views.dashboard, name='index'),
   path('holiday/', views.holiday_page, name='holiday'),
   path('login/', views.logout_page, name='login'),
   path('forgot/',views.forget_password, name='forgot'),
   path('update-user-info/<str:id>/', views.update_user, name='update-user-info'),
   path('get-user-info/<str:emp_id>/', views.get_user, name='get_user_info'), 

   path('banks/', views.bank_list, name='bank_list'),
   path('bank/<int:id>/', views.bank_detail, name='bank_detail'),
   path('bank/create/', views.bank_create, name='bank_create'),
   path('bank/<int:id>/edit/', views.edit_bank, name='edit_bank'),
   path('bank/<int:id>/delete/', views.delete_bank, name='delete_bank'),

   path('education/<int:id>/', views.education_detail, name='education_detail'),
   
]



