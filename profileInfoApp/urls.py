from django.urls import path
from .views import profile_info_view

urlpatterns = [
    path('', profile_info_view),
]
