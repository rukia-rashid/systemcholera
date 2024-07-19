
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    register_normal_user,
    street_list_create, street_detail,
    patient_list_create, patient_detail,
    health_facility_list_create, health_facility_detail,
    deceased_list_create, deceased_detail,
    recovered_list_create, recovered_detail,
    normal_user_list, register_user, 
    patient_count, recovered_patient_count, deceased_patient_count,
    user_info 
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', register_user, name='register_user'),
    path('register-normal-user/', register_normal_user, name='register_normal_user'),
    path('normal-users/', normal_user_list, name='normal_user_list'),
    path('streets/', street_list_create, name='street_list_create'),
    path('streets/<int:pk>/', street_detail, name='street_detail'),
    path('patients/', patient_list_create, name='patient_list_create'),
    path('patients/<int:pk>/', patient_detail, name='patient_detail'),
    path('health-facilities/', health_facility_list_create, name='health_facility_list_create'),
    path('health-facilities/<int:pk>/', health_facility_detail, name='health_facility_detail'),
    path('deceased/', deceased_list_create, name='deceased_list_create'),
    path('deceased/<int:pk>/', deceased_detail, name='deceased_detail'),
    path('recovered/', recovered_list_create, name='recovered_list_create'),
    path('recovered/<int:pk>/', recovered_detail, name='recovered_detail'),
    path('patient-count/', patient_count, name='patient_count'),
    path('recovered-patient-count/', recovered_patient_count, name='recovered_patient_count'),
    path('deceased-patient-count/', deceased_patient_count, name='deceased_patient_count'),
    path('auth/user/', user_info, name='user_info'),  
]
