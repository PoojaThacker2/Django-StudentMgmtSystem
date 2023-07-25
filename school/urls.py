from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# from school.views import CreateStudentView
from .views import SchoolDetail, SchoolSignUp, StudentBulkCreate, StudentFilter


urlpatterns = [
    # path('school/signup/', SchoolSignUp.as_view(), name='school-signup'),
    # path('student/bulkcreate/<int:grade>/', StudentBulkCreate.as_view(), name='student-bulkcreate'),
    # path('student/filter/<int:grade>/', StudentFilter.as_view(), name='student-filter'),
    # path('token/', TokenObtainPairView.as_view(), name='token-obtain'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    
    # path('create_student/', CreateStudentView.as_view(), name='create-student'),
    path('school/signup/', SchoolSignUp.as_view(), name='school_signup'),
    path('school/<int:pk>/', SchoolDetail.as_view(), name='school_detail'),
    path('school/bulk_create/', StudentBulkCreate.as_view(), name='bulk_create'),
    path('school/filter/', StudentFilter.as_view(), name='student_filter'),
]
