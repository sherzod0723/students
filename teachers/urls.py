from django.urls import path
from .views import TeacheraAPIVIEW, TeacherDetailAPIView, StudentRetrieveAPIView, StudentLisCReteAPIView


urlpatterns = [
    path('teachers/', TeacheraAPIVIEW.as_view(), name="teachers"),
    path('teachers/<int:pk>/', TeacherDetailAPIView.as_view(), name="teahersapi"),
    path('students/', StudentLisCReteAPIView.as_view(), name="studentsapi"),
    path('students/<int:pk>/', StudentRetrieveAPIView.as_view(), name="studentsapi")

]