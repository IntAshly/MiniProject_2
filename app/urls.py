from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... (existing url patterns)
    path('notifications/', views.notification_view, name='notifications'),
    # ... other URL patterns ...
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password/<uidb64>/<token>/', views.reset_password, name='reset_password'),
    path('', views.index_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('role/', views.role_view, name='role'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('about/', views.about, name='about'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password/<uidb64>/<token>/', views.reset_password, name='reset_password'),

    path('delete_healthcenter/<int:healthcare_provider_id>/', views.delete_healthcenter, name='delete_healthcenter'),
    path('delete-parent/<int:id>/', views.delete_parent, name='delete_parent'),


    path('health-profile_cmplt/', views.health_profile_cmplt, name='health_profile_cmplt'),
    
    path('admin_home/', views.admin_home_view, name='admin_home'),
    path('request/', views.request_view, name='request'),
    path('approve_health_center/<int:pk>/', views.approve_health_center, name='approve_health_center'),
    path('reject/<int:pk>/', views.reject_health_center, name='reject_health_center'),
    path('child_profile/', views.child_profile_view, name='child_profile'),
    path('health_home/', views.health_home_view, name='health_home'),
    path('parent_profile/', views.profile_view, name='parent_profile'),
    path('edit_parent/', views.edit_parentview, name='edit_parentview'),
    path('total_parents/', views.total_parents, name='total_parents'),
    path('total_parents/<int:user_id>/', views.total_parents, name='change_status'),
    path('total_healthcenters/', views.total_healthcenters, name='total_healthcenters'),
    path('activate_healthcenter/<int:id>/', views.activate_healthcenter, name='activate_healthcenter'),
    path('add-vaccine/', views.add_vaccine, name='add_vaccine'),
    path('view-vaccines/', views.view_vaccines, name='view_vaccines'),
   
    path('delete_vaccine/<int:vaccine_id>/', views.delete_vaccine, name='delete_vaccine'),
    path('addvaccine_req/', views.add_vaccine_request, name='addvaccine_req'),
    path('ajax/load-doses/', views.load_doses, name='ajax_load_doses'),  # AJAX URL for loading doses
    path('vaccine-request-success/', views.vaccine_request_success, name='vaccine_request_success'),  # A view to show success message
    path('delete-vaccine-request/<int:request_id>/', views.delete_vaccine_request, name='delete_vaccine_request'),
    path('vaccinereq/', views.vaccinereq_view, name='vaccinereq'),
    path('approve_vaccine_request/<int:request_id>/', views.approve_vaccine_request, name='approve_vaccine_request'),
    path('reject_vaccine_request/<int:request_id>/', views.reject_vaccine_request, name='reject_vaccine_request'),
    path('vaccine/<int:vaccine_id>/details/', views.view_vaccine_details, name='view_vaccine_details'),
    path('select_vaccine/', views.select_vaccine, name='select_vaccine'),
    path('select-healthcenter/<int:vaccine_id>/', views.select_healthcenter, name='select_healthcenter'),
    path('schedule-appointment/', views.schedule_appointment, name='schedule_appointment'),
    path('appointment-success/', views.appointment_success, name='appointment_success'),
    path('delete-appointment/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),
    path('manage-appointments/', views.manage_appointments, name='manage_appointments'),
    path('update-appointment-status/<int:appointment_id>/', views.update_appointment_status, name='update_appointment_status'),
    path('notifications/', views.notification_view, name='notification'),
    path('delete-notification/<int:notification_id>/', views.delete_notification, name='delete_notification'),
    path('healthprofile/', views.health_profile_view, name='view_healthprofile'),
    path('edit-health-profile/', views.edit_health_profile_view, name='edit_health_profile'),
    path('chart/', views.chart_view, name='chart'), 
    path('upload_image/', views.upload_image, name='upload_image'),

    path('add_feedingchart/', views.add_feedingchart, name='add_feedingchart'),
    path('feedingcharts/', views.feedingchart_lists, name='feedingchart_lists'),
    path('feedingcharts/<int:chart_id>/', views.feedingchart_details, name='feedingchart_details'),
    path('feedingchart/', views.view_feedingchart, name='view_feedingchart'),
    path('add_mentalhealth/', views.add_mentalhealth, name='add_mentalhealth'),
    path('mentalhealth_lists/', views.mentalhealth_lists, name='mentalhealth_lists'),
    path('mentalhealth/<int:mental_health_id>/', views.mentalhealth_listsdetails, name='mentalhealth_listsdetails'),
    path('mentalhealth_delete/<int:id>/', views.delete_mentalhealth, name='mentalhealth_delete'),  # Add delete path
    path('mental-health/', views.view_mentalhealth, name='view_mentalhealth'),
    path('mental-health/<int:pk>/', views.view_mentalhealthdetails, name='view_mentalhealthdetails'),
    path('vaccination-history/', views.vaccination_history, name='vaccination_history'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

