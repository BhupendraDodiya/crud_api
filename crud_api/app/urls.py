from django.urls import path
from app import views

urlpatterns = [
    path('stucreate/',views.student_create)
]
