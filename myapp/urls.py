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

   path('education/', views.education_list, name='education_list'),
   path('education/<int:id>/', views.education_detail, name='education_detail'),
   path('education/<int:id>/edit/', views.education_edit, name='education_edit'),
   path('education/<int:id>/delete/', views.delete_education, name='delete_education'),
   path('education/create/', views.education_create, name='education_create'),

   path('experience/', views.experience_list, name='experience_list'),
   path('experience/<int:id>/', views.experience_detail, name='experience_detail'),
   path('experience/create/', views.experience_create, name='experience_create'),
   path('experience/<int:id>/edit/', views.experience_edit, name='experience_edit'),
   path('experience/<int:id>/delete/', views.delete_experience, name='delete_experience'),

   path('edit/pi/', views.personal_detail, name='edit_pi'),
   path('edit/info/', views.edit_personalinfo, name='edit_personalinfo'),

   
   path('contact/detail/', views.contact_detail, name='contact_detail'),
   path('edit/contact/', views.edit_contact, name='edit_contact'),

]




