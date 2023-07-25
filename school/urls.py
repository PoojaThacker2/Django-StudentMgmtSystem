from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SchoolSignUp, StudentBulkCreate, StudentFilter

urlpatterns = [
    path('school/signup/', SchoolSignUp.as_view(), name='school-signup'),
    path('student/bulkcreate/<int:grade>/', StudentBulkCreate.as_view(), name='student-bulkcreate'),
    path('student/filter/<int:grade>/', StudentFilter.as_view(), name='student-filter'),
    path('token/', TokenObtainPairView.as_view(), name='token-obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
